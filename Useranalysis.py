# -*- coding: utf-8 -*-
import sys
import os
import pymysql
import datetime
import pandas as pd
import plotly.offline as py
import plotly.graph_objects as go
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from csvToMS import inputcsv
from DBM import dbm
from UserForm import *


class useran(QWidget, Ui_UserForm):

    #MySignal = pyqtSignal()

    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.groupBox_2.setEnabled(False)
        #self.name = self.lineEdit.text()
        self.pushButton_csv.clicked.connect(self.open_csv)
        self.pushButton_db.clicked.connect(self.open_db)
        self.pushButton_make.clicked.connect(self.plot_use)
        self.pushButton_save.clicked.connect(self.plot_save)


        plotly_dir = 'plotly_html'
        if not os.path.isdir(plotly_dir):
            os.mkdir(plotly_dir)
        self.path_plotly_html = os.getcwd() + os.sep + plotly_dir

        plot_dir = 'images'
        if not os.path.exists(plot_dir):
            os.mkdir(plot_dir)
        self.plot_path_dir = os.getcwd() + os.sep + plot_dir

    def open_csv(self):
        csv = inputcsv()
        csv.Signal.connect(self.analy)
        csv.exec_()

    def analy(self, filename):
        try:
            self.data1 = pd.read_csv(filename, nrows=1100000, names=['user_id', 'item_id',
                                                                     'category_id', 'behaviour_type',
                                                                     'timestamp'], sep=',')
            #QMessageBox.about(self, '提示', '数据正在处理中，请稍候')

            # 数据预处理
            # 删除重复值
            self.data1.drop_duplicates(keep='last', inplace=True)
            # 缺失值处理,存在缺失值则删除改行数据
            a = self.data1.isnull().sum()
            if a.sum() == 0:
                print('数据集无缺失值')
            else:
                self.data1 = self.data1.dropna(axis=0, how='any', subset=None, inplace=True)
            # 用户行为异常值
            if self.data1['behaviour_type'].nunique() == 4:
                print('行为数据无缺失值')
            else:
                QMessageBox.critical(self, '警告', '行为数据与要求不符，请检查')
            # 时间异常值
            # 将时间戳转化为北京时间
            self.data1 = self.data1.assign(
                time=pd.to_datetime(self.data1['timestamp'], unit='s') + datetime.timedelta(hours=8))
            self.data1 = self.data1[(self.data1['time'] > '2017-11-25') & (self.data1['time'] < '2017-12-4')]
        except Exception as e:
            print(e)
            QMessageBox.critical(self, '错误警告', '文件打开错误，文件可能不存在')
        else:
            QMessageBox.about(self, '提示', '文件打开并已成功导入')
            self.groupBox_2.setEnabled(True)
            self.pushButton_save.setEnabled(False)
            return self.data1

    def plot_use(self):
        self.name = self.lineEdit.text()
        if not self.name:
            QMessageBox.critical(self, '警告', '图表名输入为空')
            print(self.name)
        else:
            # 提取日期
            self.data1['date'] = self.data1['time'].dt.date
            # 日均用户数
            dfduv = self.data1[['user_id', 'date']].groupby('date').nunique()
            dfduv = dfduv.drop(columns='date')
            dfduv = dfduv.rename(columns={"user_id": "uv"})

            # 日均活跃用户数
            dfdau = self.data1[['user_id', 'behaviour_type', 'date']].groupby(['date', 'user_id']).count()
            dfdau = dfdau[dfdau['behaviour_type'] > 2]
            dfdau = dfdau.count(level=0)
            dfdau.rename(columns={'behaviour_type': 'active_user'}, inplace=True)

            # 计算日均交易用户数
            dfdbu = self.data1[self.data1['behaviour_type'] == 'buy']
            dfdbu = dfdbu[['user_id', 'behaviour_type', 'date']].groupby(['date', 'user_id']).count()
            dfdbu = dfdbu.count(level=0)
            dfdbu.rename(columns={'behaviour_type': 'buy_user'}, inplace=True)

            # 每日pv数：
            dfdpv = self.data1[['date', 'user_id']].groupby('date').count()
            dfdpv = dfdpv.rename(columns={'user_id': 'pv'})

            # 将上述各表连接后生成指标表格
            self.df1 = dfdpv.join(dfduv).join(dfdau).join(dfdbu)
            self.df1 = self.df1.assign(pv_per_user=self.df1['pv'] / self.df1['uv'],
                             active_user_rate=self.df1['active_user'] / self.df1['uv'],
                             buy_user_rate=self.df1['buy_user'] / self.df1['uv'])

            #self.comboBox_choose.currentIndexChanged.connect(self.plot_make_use)
            self.qwebengine.reload()
            self.plot_make_use()



    #def choose_confrim(self):
        #self.comboBox_choose.currentIndex = 4

    def plot_make_use(self):

        #self.current_now = self.comboBox_choose.currentIndex

        if self.comboBox_choose.currentIndex() == 1:

            path_plotly = self.path_plotly_html + os.sep + 'use_plots1.html'
            name = self.lineEdit.text()

            self.fig = go.Figure()

            self.fig.add_trace(
                go.Scatter(x=self.df1.index, y=self.df1['uv'], name="日均用户", line_color="#1f77b4")
            )
            self.fig.add_trace(
                go.Scatter(x=self.df1.index, y=self.df1['active_user'], name="日均活跃用户",
                           line_color="#ff7f0e")
            )
            self.fig.add_trace(
                go.Scatter(x=self.df1.index, y=self.df1['buy_user'], name="日均交易用户",
                           line_color="#d62728")
            )
            self.fig.update_layout(
                title_text=name)
            self.fig.update_xaxes(title_text="日期", dtick='d')

            py.plot(self.fig, filename=path_plotly, auto_open=False)
            self.qwebengine.load(QUrl.fromLocalFile(path_plotly))
            self.pushButton_save.setEnabled(True)
            print(path_plotly, name)

        elif self.comboBox_choose.currentIndex() == 2:
            path_plotly = self.path_plotly_html + os.sep + 'use_plots2.html'
            name = self.lineEdit.text()

            self.fig = go.Figure()

            self.fig.add_trace(
                go.Scatter(x=self.df1.index, y=self.df1['uv'], name="日均用户", marker=dict(color='#1f77b4'))
            )
            self.fig.add_trace(
                go.Bar(x=self.df1.index, y=self.df1['active_user_rate'], text=self.df1['active_user_rate'],
                       textposition='outside',
                       name="活跃用户比例", marker=dict(color='#ff7f0e'),
                       yaxis='y2')
            )
            self.fig.add_trace(
                go.Bar(x=self.df1.index, y=self.df1['buy_user_rate'], text=self.df1['buy_user_rate'],
                       textposition='outside',
                       name="交易用户比例", marker_color='#d62728',
                       yaxis='y2')
            )
            self.fig.update_layout(
                title_text=name,
                xaxis_title="日期",
                yaxis=dict(title="用户数", overlaying='y2', side='right'),
                yaxis2=dict(title="比例", side='left')
            )

            py.plot(self.fig, filename=path_plotly, auto_open=False)
            self.qwebengine.load(QUrl.fromLocalFile(path_plotly))
            self.pushButton_save.setEnabled(True)
            return path_plotly

        elif self.comboBox_choose.currentIndex() == 3:
            path_plotly = self.path_plotly_html + os.sep + 'use_plots3.html'
            name = self.lineEdit.text()

            df_user_active_days = self.data1[['user_id', 'behaviour_type', 'date']].groupby(
                ['date', 'user_id']).count()
            df_user_active_days = df_user_active_days[df_user_active_days['behaviour_type'] > 2]
            df_user_active_days = df_user_active_days.count(level=1)
            df_user_active_days = df_user_active_days.rename(columns={'behaviour_type': 'days'})

            self.fig = go.Figure()
            self.fig.add_trace(go.Histogram(x=df_user_active_days['days'],
                                       histnorm='percent',
                                       name="活跃天数分布图（9天内）",
                                       xbins=dict(
                                           size=0.5),
                                       marker_color='rgb(49,130,189)'
                                       )
                          )
            self.fig.update_xaxes(dtick=1)
            self.fig.update_layout(height=450, width=600, title_text=name,
                              xaxis_title="活跃天数",
                              yaxis_title="该日活跃用户占总活跃用户百分比")

            py.plot(self.fig, filename=path_plotly, auto_open=False)
            self.qwebengine.load(QUrl.fromLocalFile(path_plotly))
            self.pushButton_save.setEnabled(True)
            return path_plotly
        else:
            QMessageBox.critical(self, '错误', '选择内容为空,请重试')

    def plot_save(self):

        try:
            plot_name, dialog_action = QtWidgets.QInputDialog.getText(self, '保存图片名',
                                                                      '请输入将要保存的图片的名字',
                                                                      QtWidgets.QLineEdit.Normal)
            if self.comboBox_type.currentIndex() == 1:
                plot_path = self.plot_path_dir + os.sep + plot_name
                self.fig.write_image(plot_path + ".png")
                QMessageBox.about(self, '提示', '文件已保存在当前目录下的image文件夹中')
            elif self.comboBox_type.currentIndex() == 2:
                plot_path = self.plot_path_dir + os.sep + plot_name
                self.fig.write_image(plot_path + ".jpeg")
                QMessageBox.about(self, '提示', '文件已保存在当前目录下的image文件夹中')
            elif self.comboBox_type.currentIndex() == 3:
                plot_path = self.plot_path_dir + os.sep + plot_name
                self.fig.write_image(plot_path + ".pdf")
                QMessageBox.about(self, '提示', '文件已保存在当前目录下的image文件夹中')
            elif self.comboBox_type.currentIndex() == 4:
                plot_path = self.plot_path_dir + os.sep + plot_name
                self.fig.write_image(plot_path + ".svg")
                QMessageBox.about(self, '提示', '文件已保存在当前目录下的image文件夹中')
            else:
                QMessageBox.critical(self, '警告', '未选择图片格式')
        except Exception as e:
            print(e)
            QMessageBox.critical(self, '警告', '图片保存出现错误')

    def open_db(self):
        self.dbmanage = dbm()
        self.dbmanage.dbSignal.connect(self.analydb)
        self.dbmanage.exec_()

    def analydb(self, dbhost, dbport, dbuser, dbpsw, dbname, txt_name):
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
        except Exception as e:
            print(e)
            QMessageBox.critical(self, '警告', '数据库连接失败')
        else:
            QMessageBox.about(self, '提示', '数据库连接成功')
            self.dbmanage.connButton.setEnabled(False)
            self.dbmanage.outButton.setEnabled(True)

        # 数据预处理
        # 重复值处理
        self.data1.drop_duplicates(keep='last', inplace=True)
        # 缺失值处理
        a = self.data1.isnull().sum()
        if a.sum() == 0:
            print('数据集无缺失值')
        else:
            self.data1 = self.data1.dropna(axis=0, how='any', subset=None, inplace=True)
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

        self.groupBox_2.setEnabled(True)
        self.pushButton_csv.setEnabled(True)
        return self.data1



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ua = useran()
    ua.show()
    sys.exit(app.exec_())
