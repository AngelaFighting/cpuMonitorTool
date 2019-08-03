#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from matplotlib import pyplot as plt
import csv
import datetime

from tools.configUtil import ConfigUtil


class ChartUtil():

    def __init__(self, configData):
        self.configData = configData

    def getData(self, fileName, type):
        with open(fileName) as csvfile:
            reader = csv.reader(csvfile)
            header_row = next(reader)  # 跳过标题行
            x_times = []
            y_values = []
            for i in reader:
                time = datetime.datetime.strptime(i[0], "%Y-%m-%d %H:%M:%S")
                if time >= configData.get('startTime') and time <= configData.get('endTime'):
                    x_times.append(time)
                    if 'CPU' == type:
                        value = float(i[1])
                        y_values.append(value)
                    else:
                        value = float(i[2])
                        y_values.append(value)
            return x_times, y_values

    def drawChart(self, type):
        plt.title(type + '_Time_Line')
        plt.figure(figsize=(15, 8))
        lines = self.configData.get('lines')
        for line in lines:
            ip = list(line.keys())[0]
            fileName = str(ip) + '.csv'
            x_times, y_values = self.getData(fileName, type)
            plt.plot(x_times, y_values, linewidth=1, color=line.get(ip), label=ip)
        plt.legend()
        plt.xlabel('Time')
        plt.ylabel(type + ' Used %')
        plt.xticks(color='green', rotation=80)
        plt.subplots_adjust(bottom=0.3)  # 调整图形的位置
        plt.savefig(type + "Picture")


if __name__ == '__main__':
    configUtil = ConfigUtil()
    configData = configUtil.readConfig()
    # 绘制图表
    chartUtil = ChartUtil(configData)
    chartUtil.drawChart('CPU')
    chartUtil.drawChart('Memory')
