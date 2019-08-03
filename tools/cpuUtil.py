#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import psutil
import datetime
import csv
import logging
import time

from tools.configUtil import ConfigUtil


class CPUUtil():

    def __init__(self, saveFilename="cpuInfo.csv", sleepTime=10):
        '''
        初始化信息
        :param saveFilename: 保存的文件名
        :param sleepTime: 获取间隔频率，单位s
        '''
        self.saveFilename = saveFilename
        self.sleepTime = sleepTime

    def getCpu(self):
        logging.basicConfig(filename='log.txt', level=logging.DEBUG, format='%(asctime)s-%(levelname)s-%(message)s')
        count = 0  # 迭代统计次数
        startflag = True

        while True:
            if startflag:
                logging.info("----------startflag = True---------")
                csvFile = open(self.saveFilename, "w")
                writer = csv.writer(csvFile)
                writer.writerow(["datetime", "cpuused", "mempercent"])
                startflag = False
                csvFile.close()
            else:
                logging.info("----------count: " + str(count) + "---------")
                try:
                    datetimeValue = datetime.datetime.strftime(datetime.datetime.now(),
                                                               '%Y-%m-%d %H:%M:%S')  # 日期 时间
                    cpu = psutil.cpu_percent(1, False)  # cpu使用率
                    mempercent = psutil.virtual_memory().percent  # 内存使用率
                    logging.info("datetime:" + datetimeValue + " cpu:" + str(cpu) + " mempercent:" + str(mempercent))
                    csvFile = open(self.saveFilename, "a")
                    writer = csv.writer(csvFile)
                    writer.writerow([datetimeValue, str(cpu), str(mempercent)])
                    count = count + 1
                    csvFile.close()
                    time.sleep(self.sleepTime)
                except Exception as e:
                    logging.error(e)


if __name__ == '__main__':
    configUtil = ConfigUtil()
    configData = configUtil.readConfig()
    cpuUtil = CPUUtil(saveFilename=configData.get('saveFilename'), sleepTime=configData.get('sleepTime'))
    cpuUtil.getCpu()
