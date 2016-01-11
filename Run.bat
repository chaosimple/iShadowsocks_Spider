@ echo off 

echo stop shadowsocks
@ taskkill /f /t /im Shadowsocks.exe

echo start spider
scrapy crawl SSSpider

echo update config file
python updateConfig.py

echo start shadowsocks
START "shadowsocks" "D:\Program Files\shadowsocks\Shadowsocks.exe"
pause