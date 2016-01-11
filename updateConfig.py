#!/usr/bin/env python
#coding:utf-8
"""
  Author : Chaos--<chaosimpler@gmail.com>
  Purpose: 
  Created: 2016/1/10
"""

#from scrapy.crawler import CrawlerProcess
#from scrapy.utils.project import get_project_settings
import json, os, shutil

configFile = r'D:\Program Files\Shadowsocks\gui-config.json'
downloadInfoFile = 'Result.json'
backupConfigFile = 'BackupConfig.json'

#----------------------------------------------------------------------
def crawl_Info():
    """
    该函数用于从http://www.ishadowsocks.com/网站上爬取免费SHADOWSOCKS帐号
    结果存储在Result.json文件中
    """
    process = CrawlerProcess(get_project_settings())
    process.crawl('SSSpider')
    process.start()
    
    
    

#----------------------------------------------------------------------
def updateConfig():
    """"""
    #如果配置文件不存在，先使用备份的配置文件
    if not os.path.exists(configFile):
        shutil.copy(os.path.join(os.getcwd(),backupConfigFile), configFile)
        
    with open(downloadInfoFile, 'r') as rf:
        #1 先读取从互联网上获取的数据
        Info = json.load(rf)
        
        with open(configFile, 'r') as cf:
            #2 读取配置文件
            obj = json.load(cf)
            
            #3 用从网络上爬取的数据设置新的值
            config = obj['configs'][0]
            config['password'] = Info['password']
            config['server'] = Info['server']
            config['port'] = Info['port']
            config['method'] = Info['method']
            
            #4 保存配置文件
            with open(backupConfigFile, 'w') as tp:
                line = json.dumps(dict(obj)) + "\n"
                tp.write(line)
    
    #5 将更新后的配置文件复制到程序目录
    os.remove(configFile)
    shutil.copy(os.path.join(os.getcwd(), backupConfigFile), configFile)
    
    print 'update config over!'    

if __name__ == '__main__':
    
    #从网上爬取数据
    #crawl_Info()
    #更新配置文件
    updateConfig()
    
    print 'over'
    
   
    
    
