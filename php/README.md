### #php

```
# 卸载旧版本

$ yum remove php*

# 安装PHP7及其插件
$ rpm -Uvh https://mirror.webtatic.com/yum/el7/webtatic-release.rpm

$ yum install php70w-common php70w php70w-opcache php70w-gd php70w-mysqlnd php70w-mbstring php70w-devel

```

```
php内置开发服务器:
  # 简单启动
  php -S localhost:8080
  # 指定配置文件
  php -S localhost:8000 -c app/config/php.ini
  # 根据路由文件启动
  php -S localhost:8000 router.php

```

### #php包管理工具

和很多编程语言一样，php也有自己的包管理工具。php的包管理工具最流行也是最常用的是:Composer

1. Composer的安装与使用

```
# 安装
$ curl -sS https://getcomposer.org/installer | php

# composer安装完成之后只能使用php调用，没有作为全局命令安装，如果想要作为全局命令使用则需要执行:
mv composer.phar /usr/local/bin/composer

# 用composer 创建一个空项目，该项目中只有composer.json文件，里面是对项目的描述
$ composer init --require=foo/bar:1.0.0 -n
{
    "require": {
        "foo/bar": "1.0.0"
    }
}

# 使用 Composer
# 安装项目依赖
# 该命令会自动读取项目下的composer.json文件中的依赖关系，然后安装，类似于npm中的package.json文件
# 该命令类似于npm install 或者 pip install -r requirements.txt
$ composer install

# php依赖关系文件composer.json
{
    "require": {
        "monolog/monolog": "1.2.*"
    }
}

# 更新项目依赖
$ composer update

# 配置国内镜像
$ composer config -g repo.packagist composer https://packagist.laravel-china.org

# 解除镜像
$ composer config -g --unset repos.packagist


```

### #PHP框架

1. [PHP框架](https://zh.wikipedia.org/wiki/PHP%E6%A1%86%E6%9E%B6%E5%88%97%E8%A1%A8)


