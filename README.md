# 测试flask + sqlalchemy + sqlite/postgres搭建mvc框架

* 使用python做Web后台较少
* flask搭建mvc的实践分享更少
* 创建仓库，用于分享使用flask搭建mvc

## 安装依赖

```shell
pip install -r requirements.txt
```

## 结构

* root
    * common
        * libs 工具类相关
        * models 模型
        * database 数据库
    * config
        settings.py 全局变量类（一般使用docker，所以变量全都使用环境变量设置）
    * controllers
        * api
            * user_api.py 用户api（前后端分离开发）
        * index.py 页面路由
    * interceptors 拦截器
        * all.py 可以放置权限、数据库初始化
        * error_handler.py 错误处理
    * temp 临时文件，如sqlite文件
    * templates 页面
        * common
            * layout.html
        *index.html
    * application.py 主程序
    * requirements.txt 依赖


## 参考文档
> https://blog.csdn.net/qq78442761/article/details/104555262