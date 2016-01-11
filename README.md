# SS_Spider
该系统使用scrapy框架爬取ishadowsocks网站上的服务器、端口和密码等信息。

通过运行updateConfig.py脚本可以自动从[网站](http://www.ishadowsocks.com/)上爬取免费的账号信息，并更新到软件的配置文件中（需要在updateConfig.py中设置软件的配置文件目录项：configFile ）。

---
### 更新历史
##### 2016年1月11日14:51:02
1. 修改updateConfig.py和Run.bat，修改运行方式：
	- 对于爬虫，通过bat文件直接从命令行中启动；
	- 在updateConfig.py中直接使用爬虫结果来更新配置文件。
2. 修改Run.bat，系统运行流程变为：
	- 关闭正在运行的Shadowsocks程序；
	- 启动爬虫爬取网站上的免费账号信息；
	- 调用updateConfig.py修改配置文件信息；
	- 重新启动Shadowsocks程序。


##### 2016年1月11日
1. 修改Item.py，将所有的项改为小写，并增加method项。
2. 修改sp.py，只爬取服务器A的信息。
3. 修改pipelines.py，将爬取的信息直接保存为json格式文件`Result.json`。
4. 将test.py修改为updateConfig.py，增加对配置文件的修改逻辑，可以从网上下载免费账号信息后自动修改程序的配置文件；增加了配置文件的备份：`BackupConfig.json`。


