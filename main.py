# -*- coding: utf-8 -*-
import sys
import os
import pymysql
import datetime
import pandas as pd
import numpy as np
import plotly.offline as py
import plotly.graph_objects as go
from Mainmenu import *
from Useranalysis import *
from RoutineForm import *
from TimeForm import *
from ItemForm import *
from csvToMS import inputcsv
from DBM import dbm
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QDialog, QMessageBox
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import *




class mainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.P = 0

        self.user = useran()
        self.userButton.clicked.connect(self.user_show)
        self.routine = routineForm()
        self.routineButton.clicked.connect(self.routine_show)
        self.time = timeForm()
        self.timeButton.clicked.connect(self.time_show)
        self.item = itemForm()
        self.itemButton.clicked.connect(self.item_show)

        self.action_Input_csv.triggered.connect(self.csv_show)
        self.action_Input_DataBase_3.triggered.connect(self.db_show)
        self.action_Quit.triggered.connect(self.close)

        plotly_dir = 'plotly_html'
        if not os.path.isdir(plotly_dir):
            os.mkdir(plotly_dir)
        self.path_plotly_html = os.getcwd() + os.sep + plotly_dir

        plot_dir = 'images'
        if not os.path.exists(plot_dir):
            os.mkdir(plot_dir)
        self.plot_path_dir = os.getcwd() + os.sep + plot_dir

    def csv_show(self):
        csv = inputcsv()
        csv.Signal.connect(self.analycsv_pre)
        csv.exec_()

    def db_show(self):
        self.dbmanage = dbm()
        self.dbmanage.dbSignal.connect(self.analydb_pre)
        self.dbmanage.exec_()

    def analycsv_pre(self, filename):
        try:
            self.data1 = pd.read_csv(filename, nrows=1100000, names=['user_id', 'item_id', 'category_id', 'behaviour_type',
                                                                     'timestamp'], sep=',')
            # 数据预处理
            # 删除重复值
            self.data1.drop_duplicates(keep='last', inplace=True)
            # 缺失值处理,存在缺失值则删除改行数据
            a = self.data1.isnull().sum()
            if a.sum() == 0:
                print('数据集无缺失值')
            else:
                self.data1 = self.data1.dropna(axis=0, how='any', subset=None, inplace=False)
            # 用户行为异常值
            if self.data1['behaviour_type'].nunique() == 4:
                print('行为数据无缺失值')
            else:
                QMessageBox.critical(self, '警告', '行为数据与要求不符，请检查')
            # 时间异常值
            # 将时间戳转化为北京时间(到秒)
            self.data1 = self.data1.assign(
                time=pd.to_datetime(self.data1['timestamp'], unit='s') + datetime.timedelta(hours=8))
            self.data1 = self.data1[(self.data1['time'] > '2017-11-25') & (self.data1['time'] < '2017-12-4')]

        except Exception as e:
            print(e)
            QMessageBox.critical(self, '错误警告', '文件打开错误，文件可能不存在')
        else:
            QMessageBox.about(self, '提示', '文件打开并已成功导入')
            self.P = 1
            return self.data1

    def analydb_pre(self, dbhost, dbport, dbuser, dbpsw, dbname, txt_name):
        try:
            # 连接数据库
            conn = pymysql.connect(host=dbhost,
                                   port=dbport,
                                   user=dbuser,
                                   passwd=dbpsw,
                                   db=dbname,
                                   charset="utf8")
            sql = "SELECT * FROM %s" % txt_name
            self.data1 = pd.read_sql(sql, conn)
            # 重复值处理
            self.data1.drop_duplicates(keep='last', inplace=True)
            # 缺失值处理
            a = self.data1.isnull().sum()
            if a.sum() == 0:
                print('数据集无缺失值')
            else:
                print(a[a > 0])
            # 用户行为异常值
            if self.data1['behaviour_type'].nunique() == 4:
                print('行为数据无缺失值')
            else:
                QMessageBox.critical(self, '警告', '数据行为存在缺失值，请检查')
            # 时间异常值
            # 将时间戳转化为北京时间
            self.data1 = self.data1.assign(
                time=pd.to_datetime(self.data1['timestamp'], unit='s') + datetime.timedelta(hours=8))
            self.data1 = self.data1[(self.data1['time'] > '2017-11-25') & (self.data1['time'] < '2017-12-4')]
        except Exception as e:
            print(e)
            QMessageBox.critical(self, '警告', '数据库连接失败')
            self.P = 0
        else:
            QMessageBox.about(self, '提示', '数据库连接成功')
            self.P = 1
            self.dbmanage.connButton.setEnabled(False)
            self.dbmanage.outButton.setEnabled(True)
            return self.data1

    def routine_show(self):
        if self.P == 1:
            self.routine.pushButton_db.setEnabled(False)
            self.routine.pushButton_csv.setEnabled(False)
            self.routine.pushButton_make.setEnabled(True)
            self.routine.pushButton_save.setEnabled(False)
            self.routine.pushButton_quit.clicked.connect(self.close_event)
            self.routine.pushButton_make.clicked.connect(self.routine_pre)
            self.routine.pushButton_save.clicked.connect(self.plot_save_routine)
            self.routine.show()
        elif self.P == 0:
            self.routine.pushButton_quit.clicked.connect(self.close_event)
            self.routine.pushButton_csv.clicked.connect(self.csv_show)
            self.routine.pushButton_db.clicked.connect(self.db_show)
            self.routine.pushButton_make.clicked.connect(self.routine_pre)
            self.routine.pushButton_save.clicked.connect(self.plot_save_routine)
            self.routine.show()

    def routine_pre(self):
        self.routine.name_routine = self.routine.lineEdit.text()
        if not self.routine.name_routine :
            QMessageBox.critical(self, '警告', '图表名输入为空')
        else:
            df = self.data1
            pv_users = df[df['behaviour_type'] == 'pv']['user_id'].count()
            fav_users = df[df['behaviour_type'] == 'fav']['user_id'].count()
            cart_users = df[df['behaviour_type'] == 'cart']['user_id'].count()
            buy_users = df[df['behaviour_type'] == 'buy']['user_id'].count()
            self.text = ['点击', '加入购物车', '收藏', '购买']
            self.values = [np.around((pv_users / pv_users * 100), 2),
                           np.around((cart_users / pv_users * 100), 2),
                           np.around((fav_users / pv_users * 100), 2),
                           np.around((buy_users / pv_users * 100), 2)]
            self.plot_make_routine()

    def plot_make_routine(self):
        path_plotly = self.path_plotly_html + os.sep + 'routine_plot.html'
        name = self.routine.lineEdit.text()

        self.fig = go.Figure()
        self.fig.add_trace(
            go.Funnel(
                x=self.values,
                y=self.text,
                textinfo="value+percent initial", textposition='inside',
                marker=dict(color=['#b0a4e3', '#cca4e3', '#edd1d8', '#e4c6d0'])
            )
        )
        self.fig.update_layout(
            title_text=name
        )
        py.plot(self.fig, filename=path_plotly, auto_open=False)
        self.routine.qwebengine.load(QUrl.fromLocalFile(path_plotly))
        self.routine.pushButton_save.setEnabled(True)


    def user_show(self):
        if self.P == 1:
            self.user.pushButton_db.setEnabled(False)
            self.user.pushButton_csv.setEnabled(False)
            self.user.groupBox_2.setEnabled(True)
            self.user.pushButton_make.setEnabled(True)
            self.user.pushButton_save.setEnabled(False)
            self.user.data1 = self.data1
            self.user.pushButton_quit.clicked.connect(self.close_event)
            self.user.show()
        if self.P == 0:
            self.user.pushButton_quit.clicked.connect(self.close_event)
            #self.user.pushButton_csv.clicked.connect(self.csv_show)
            #self.user.pushButton_db.clicked.connect(self.db_show)
            self.user.show()

    def time_show(self):
        if self.P == 1:
            self.time.pushButton_db.setEnabled(False)
            self.time.pushButton_csv.setEnabled(False)
            self.time.pushButton_make.setEnabled(True)
            self.time.pushButton_save.setEnabled(False)
            self.time.pushButton_quit.clicked.connect(self.close_event)
            self.time.pushButton_make.clicked.connect(self.time_plot_pre)
            self.time.pushButton_save.clicked.connect(self.plot_save_time)
            self.time.show()
        elif self.P == 0:
            self.user.pushButton_quit.clicked.connect(self.close_event)
            self.time.pushButton_csv.clicked.connect(self.csv_show)
            self.time.pushButton_db.clicked.connect(self.db_show)
            self.time.pushButton_make.clicked.connect(self.time_plot_pre)
            self.time.pushButton_save.clicked.connect(self.plot_save_time)
            self.time.show()

    def time_plot_pre(self):
        self.time.name_time = self.time.lineEdit.text()
        if not self.time.name_time:
            QMessageBox.critical(self, '警告', '图表名输入为空')
        else:
            if self.time.comboBox_choose.currentIndex() == 1:
                # 用户活跃时间分布，划分成24小时，求9天的总和
                df43 = self.data1
                df43['hour'] = df43['time'].dt.hour

                # pv数
                self.df431_pv = df43[['hour', 'user_id']].groupby('hour').count()
                self.df431_pv.rename(columns={'user_id': '访问数'}, inplace=True)

                # uv数
                self.df431_uv = df43[['hour', 'user_id']].groupby('hour').nunique()
                self.df431_uv = self.df431_uv.drop(columns='hour')
                self.df431_uv.rename(columns={'user_id': '用户数'}, inplace=True)

                # 购买数
                self.df431_buy = df43[df43['behaviour_type'] == 'buy']
                self.df431_buy = self.df431_buy[['hour', 'user_id']].groupby('hour').count()
                self.df431_buy.rename(columns={'user_id': '购买数'}, inplace=True)

                self.time_plot_make()

            elif self.time.comboBox_choose.currentIndex() == 2:
                self.data1['hour'] = self.data1['time'].dt.hour
                self.hour_buy_user_num = self.data1[self.data1['behaviour_type' \
                                                               ''] == 'buy'].drop_duplicates([
                    'user_id','hour']).groupby('hour')['user_id'].count()
                self.hour_active_user_num = self.data1.drop_duplicates(['user_id',
                                                                        'hour']).groupby('hour')['user_id'].count()
                self.hour_buy_rate = self.hour_buy_user_num / self.hour_active_user_num
                self.time_plot_make()

    def time_plot_make(self):
        if self.time.comboBox_choose.currentIndex() == 1:
            path_plotly = self.path_plotly_html + os.sep + 'time_plots1.html'
            name = self.time.lineEdit.text()

            self.fig = go.Figure()

            self.fig.add_trace(
                go.Bar(x=self.df431_pv.index, y=self.df431_pv['访问数'],
                       name="日pv时间分布",
                       marker=dict(color='#b0a4e3')
                       ))
            self.fig.add_trace(
                go.Scatter(x=self.df431_uv.index, y=self.df431_uv['用户数'],
                           name="日用户数时间分布",
                           marker=dict(color='#1685a9'),
                           yaxis='y2'
                           ))
            self.fig.add_trace(
                go.Scatter(x=self.df431_buy.index, y=self.df431_buy['购买数'],
                           name="日购买数时间分布",
                           marker=dict(color='#0c8918'),
                           yaxis='y2'
                           ))
            self.fig.update_layout(
                title_text=name,
                legend=dict(x=0.1, y=1),
                xaxis_title="时间",
                yaxis2=dict(overlaying='y1', side='right')
            )
            py.plot(self.fig, filename=path_plotly, auto_open=False)
            self.time.qwebengine.load(QUrl.fromLocalFile(path_plotly))
            self.time.pushButton_save.setEnabled(True)
            return path_plotly

        elif self.time.comboBox_choose.currentIndex() == 2:
            path_plotly = self.path_plotly_html + os.sep + 'time_plots2.html'
            name = self.time.lineEdit.text()

            self.fig = go.Figure()
            self.fig.add_trace(
                go.Scatter(x=self.hour_active_user_num.index,
                           y=self.hour_active_user_num.values,
                           name="时购买人数",
                           line_color="#1f77b4",
                           yaxis='y1'
                           )
            )
            self.fig.add_trace(
                go.Scatter(x=self.hour_buy_rate.index,
                           y=self.hour_buy_rate.values,
                           name="时购买率",
                           line_color="#ff7f0e",
                           yaxis='y2'
                           )
            )
            self.fig.update_xaxes(dtick=1)
            self.fig.update_layout(
                title_text=name,
                xaxis_title="时间",
                yaxis1=dict(overlaying='y2', side='left'),
                yaxis2=dict(side='right')
            )
            py.plot(self.fig, filename=path_plotly, auto_open=False)
            self.time.qwebengine.load(QUrl.fromLocalFile(path_plotly))
            self.time.pushButton_save.setEnabled(True)
            return path_plotly
        else:
            QMessageBox.critical(self, '错误', '选择内容为空,请重试')

    def item_show(self):
        if self.P == 1:
            self.item.pushButton_db.setEnabled(False)
            self.item.pushButton_csv.setEnabled(False)
            self.item.pushButton_make.setEnabled(True)
            self.item.pushButton_save.setEnabled(False)
            self.item.pushButton_quit.clicked.connect(self.close_event)
            self.item.pushButton_make.clicked.connect(self.item_pre)
            self.item.pushButton_save.clicked.connect(self.plot_save_item)
            self.item.show()
        elif self.P == 0:
            self.item.pushButton_quit.clicked.connect(self.close_event)
            self.item.pushButton_csv.clicked.connect(self.csv_show)
            self.item.pushButton_db.clicked.connect(self.db_show)
            self.item.pushButton_make.clicked.connect(self.item_pre)
            self.item.pushButton_save.clicked.connect(self.plot_save_item)
            self.item.show()

    def item_pre(self):
        self.item.name_item = self.item.lineEdit.text()
        if self.item.name_item is None:
            QMessageBox.critical(self, '警告', '图表名输入为空')
        else:
            self.data1_buy = self.data1[self.data1['behaviour_type'] == 'buy']

            # 聚合计数每商品大类的交易数
            self.data1_buy_category = self.data1_buy[['category_id',
                                                      'behaviour_type']].groupby('category_id').count()
            self.data1_buy_category = self.data1_buy_category.rename(columns={'behaviour_type': 'buy_count'})

            # 排序
            self.data1_buy_category = self.data1_buy_category.sort_values('buy_count', ascending=False)
            self.data1_buy_category = self.data1_buy_category.reset_index()

            self.plot_item_make()

    def plot_item_make(self):
        if self.item.comboBox_choose.currentIndex() == 1:
            path_plotly = self.path_plotly_html + os.sep + 'item_plots1.html'
            name = self.item.lineEdit.text()

            self.data1_buy_category = self.data1_buy_category[self.data1_buy_category.index < 20]

            self.fig = go.Figure(data=[go.Pie(labels=self.data1_buy_category['category_id'],
                                         values=self.data1_buy_category['buy_count'])])
            self.fig.update_traces(
                hoverinfo='label+percent', textinfo='value')
                #marker=dict(line=dict(color='#000000', width=2)))
            self.fig.update_layout(
                title_text=name
            )
            py.plot(self.fig, filename=path_plotly, auto_open=False)
            self.item.qwebengine.load(QUrl.fromLocalFile(path_plotly))
            self.item.pushButton_save.setEnabled(True)
            return path_plotly

        if self.item.comboBox_choose.currentIndex() == 2:
            path_plotly = self.path_plotly_html + os.sep + 'item_plots2.html'
            name = self.item.lineEdit.text()

            # 有购买行为的商品大类与原始数据连接，可得到以用户id及商品大类id为键的包含其他行为数据的dataframe，并聚合计数其行为数据
            data1_behav_category = pd.merge(self.data1_buy[['user_id',
                                                            'category_id']],
                                            self.data1, on=['user_id', 'category_id'],
                                            how='left')
            data1_behav_category = data1_behav_category[['category_id', 'behaviour_type']].groupby(
                'category_id').count()
            data1_behav_category = data1_behav_category.rename(columns={'behaviour_type': 'behav_count'})
            data1_behav_category = data1_behav_category.reset_index()

            # 只分析最终有购买的用户行为，与上一步商品大类交易数占比中的dataframe连接，计算比值
            df_cate_buy_behav = pd.merge(self.data1_buy_category, data1_behav_category,
                                         on='category_id', how='inner')
            df_cate_buy_behav = df_cate_buy_behav.assign(
                behav_per_buy=df_cate_buy_behav['behav_count'] / df_cate_buy_behav['buy_count'])

            self.fig = go.Figure()
            self.fig.add_trace(
                go.Scatter(x=df_cate_buy_behav['behav_per_buy'],
                           y=df_cate_buy_behav['buy_count'],
                           mode='markers',
                           marker=dict(size=16,
                                       color=np.random.randn(5000),
                                       colorscale='Viridis',
                                       showscale=True)
                           )
            )
            self.fig.update_layout(title_text=name,
                                   xaxis_title="平均行为数/购买",
                                   yaxis_title="购买数",
                              yaxis_zeroline=False, xaxis_zeroline=False)

            py.plot(self.fig, filename=path_plotly, auto_open=False)
            self.item.qwebengine.load(QUrl.fromLocalFile(path_plotly))
            self.item.pushButton_save.setEnabled(True)
            return path_plotly
        else:
            QMessageBox.critical(self, '错误', '选择内容为空,请重试')

    def plot_save_time(self):
        plot_name, dialog_action = QtWidgets.QInputDialog.getText(self, '保存图片名', '请输入将要保存的图片的名字', QtWidgets.QLineEdit.Normal)
        try:
            if self.time.comboBox_type.currentIndex() == 1:
                plot_path = self.plot_path_dir + os.sep + plot_name
                self.fig.write_image(plot_path + ".png")
                QMessageBox.about(self, '提示', '文件已保存在当前目录下的image文件夹中')
            elif self.time.comboBox_type.currentIndex() == 2:
                plot_path = self.plot_path_dir + os.sep + plot_name
                self.fig.write_image(plot_path + ".jpeg")
                QMessageBox.about(self, '提示', '文件已保存在当前目录下的image文件夹中')
            elif self.time.comboBox_type.currentIndex() == 3:
                plot_path = self.plot_path_dir + os.sep + plot_name
                self.fig.write_image(plot_path + ".pdf")
                QMessageBox.about(self, '提示', '文件已保存在当前目录下的image文件夹中')
            elif self.time.comboBox_type.currentIndex() == 4:
                plot_path = self.plot_path_dir + os.sep + plot_name
                self.fig.write_image(plot_path + ".svg")
                QMessageBox.about(self, '提示', '文件已保存在当前目录下的image文件夹中')
            else:
                QMessageBox.critical(self, '警告', '未选择图片格式')
        except Exception as e:
            print(e)
            QMessageBox.critical(self, '警告', '图片保存出现错误')

    def plot_save_routine(self):
        plot_name, dialog_action = QtWidgets.QInputDialog.getText(self, '保存图片名', '请输入将要保存的图片的名字', QtWidgets.QLineEdit.Normal)
        try:
            if self.routine.comboBox_type.currentIndex() == 1:
                plot_path = self.plot_path_dir + os.sep + plot_name
                self.fig.write_image(plot_path + ".png")
                QMessageBox.about(self, '提示', '文件已保存在当前目录下的image文件夹中')
            elif self.routine.comboBox_type.currentIndex() == 2:
                plot_path = self.plot_path_dir + os.sep + plot_name
                self.fig.write_image(plot_path + ".jpeg")
                QMessageBox.about(self, '提示', '文件已保存在当前目录下的image文件夹中')
            elif self.routine.comboBox_type.currentIndex() == 3:
                plot_path = self.plot_path_dir + os.sep + plot_name
                self.fig.write_image(plot_path + ".pdf")
                QMessageBox.about(self, '提示', '文件已保存在当前目录下的image文件夹中')
            elif self.routine.comboBox_type.currentIndex() == 4:
                plot_path = self.plot_path_dir + os.sep + plot_name
                self.fig.write_image(plot_path + ".svg")
                QMessageBox.about(self, '提示', '文件已保存在当前目录下的image文件夹中')
            else:
                QMessageBox.critical(self, '警告', '未选择图片格式')
        except Exception as e:
            print(e)
            QMessageBox.critical(self, '警告', '图片保存出现错误')

    def plot_save_item(self):
        plot_name, dialog_action = QtWidgets.QInputDialog.getText(self, '保存图片名', '请输入将要保存的图片的名字', QtWidgets.QLineEdit.Normal)
        try:
            if self.item.comboBox_type.currentIndex() == 1:
                plot_path = self.plot_path_dir + os.sep + plot_name
                self.fig.write_image(plot_path + ".png")
                QMessageBox.about(self, '提示', '文件已保存在当前目录下的image文件夹中')
            elif self.item.comboBox_type.currentIndex() == 2:
                plot_path = self.plot_path_dir + os.sep + plot_name
                self.fig.write_image(plot_path + ".jpeg")
                QMessageBox.about(self, '提示', '文件已保存在当前目录下的image文件夹中')
            elif self.item.comboBox_type.currentIndex() == 3:
                plot_path = self.plot_path_dir + os.sep + plot_name
                self.fig.write_image(plot_path + ".pdf")
                QMessageBox.about(self, '提示', '文件已保存在当前目录下的image文件夹中')
            elif self.item.comboBox_type.currentIndex() == 4:
                plot_path = self.plot_path_dir + os.sep + plot_name
                self.fig.write_image(plot_path + ".svg")
                QMessageBox.about(self, '提示', '文件已保存在当前目录下的image文件夹中')
            else:
                QMessageBox.critical(self, '警告', '未选择图片格式')
        except Exception as e:
            print(e)
            QMessageBox.critical(self, '警告', '图片保存出现错误')

    def close_event(self):
        sys.exit(app)



class routineForm(QWidget, Ui_RoutineForm):

    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.name_routine = self.lineEdit.text()



class timeForm(QWidget, Ui_TimeForm):

    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        #self.groupBox_2.setEnabled(False)
        self.name_time = self.lineEdit.text()



class itemForm(QWidget, Ui_ItemForm):

    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.name_item = self.lineEdit.text()






if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = mainWindow()
    main.show()
    sys.exit(app.exec_())







