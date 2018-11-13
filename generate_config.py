#!/usr/bin/env python
# -*- coding: utf-8 -*-


import json

# test_dict = {'bigberg': [7600, {1: [['iPhone', 6300], ['Bike', 800], ['shirt', 300]]}]}

config_dict={"server":"0.0.0.0","server_port":1090,"local_address":"127.0.0.1",
             "local_port":1080, "password":"90970306Cyq", "timeout":300, "method":"aes-256-cfb",
             "fast_open":"false", "workers": 1}


print(config_dict)
print(type(config_dict))

#dumps 将数据转换成字符串
json_str = json.dumps(config_dict)
print(json_str)
print(type(json_str))

#loads: 将 字符串 转换为 字典
new_dict = json.loads(json_str)
print(new_dict)
print(type(new_dict))

#dump: 将数据写入json文件中
with open("config/config.json","w") as f:
     json.dump(new_dict,f)
     print("加载入文件完成...")


#load:把文件打开，并把字符串变换为数据类型
with open("config/config.json",'r') as load_f:
    load_dict = json.load(load_f)
    print(load_dict)
