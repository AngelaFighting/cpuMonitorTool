#!/usr/bing/env python
# -*- coding: UTF-8 -*-
import yaml


class ConfigUtil():

    def readConfig(self):
        with open("config.yml", "r", encoding="utf-8") as f:
            yml_data = f.read()
            # load方法转出为字典类型
            data = yaml.load(yml_data)
            print(data)
            return data
