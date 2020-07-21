# [云测速](http://cloudping.bastionhost.org/) &nbsp; [![Tweet](https://img.shields.io/twitter/url/http/shields.io.svg?style=social)](https://twitter.com/intent/tweet?text=This%20site%20allows%20you%20to%20perform%20an%20HTTP%20ping%20to%20measure%20the%20network%20latency%20from%20your%20browser%20to%20the%20various%20cloud%20data%20centers%20around%20the%20world.&url=http://cloudping.bastionhost.org/en/&via=github&hashtags=cloudping,cloud,latency,aws,azure,aliyun,developers)

[![Price](https://img.shields.io/badge/price-FREE-0098f7.svg)](https://github.com/bastionhost/cloudping/blob/master/LICENSE) &nbsp; [![Build Status](https://travis-ci.org/bastionhost/cloudping.png?branch=master)](https://travis-ci.org/bastionhost/cloudping)

本项目通过 `HTTP Ping` 测量你的浏览器至全球各个云节点的网络延迟。

![demo](./media/screenshot.png)

访问 http://cloudping.bastionhost.org/ 以查看所有云节点

主要包含如下应用:

* ping - 主要逻辑都在这个应用下

## 安装

为了快速进入开发，请先安装 Python 2.x，并构建虚拟环境

`mkvirtualenv cloudping`

安装依赖

`pip install -r requirements.txt`

运行服务

`python manage.py runserver --settings=cloudping.settings.dev`

## 公有云节点

* AWS: http://ec2-reachability.amazonaws.com/
* Microsoft Azure: https://azure.microsoft.com/zh-cn/regions/
* 阿里云: https://help.aliyun.com/document_detail/40654.html
* 谷歌云: https://cloud.google.com/compute/docs/regions-zones/
* 腾讯云: https://cloud.tencent.com/document/product/213/6091
* 百度云: https://cloud.baidu.com/doc/BOS/S3.html#.E6.9C.8D.E5.8A.A1.E5.9F.9F.E5.90.8D
* 华为云: https://support.huaweicloud.com/obs/index.html
* 金山云: https://docs.ksyun.com/directories/1782
* 七牛云: https://developer.qiniu.com/kodo/manual/1671/region-endpoint
* 青云: https://docs.qingcloud.com/qingstor/api/common/overview.html#地址构成
* UCloud: https://docs.ucloud.cn/api/summary/regionlist
* 美团云: https://www.mtyun.com/doc/products/manage/Region/index
* Digital Ocean: http://speedtest-nyc1.digitalocean.com/
* Linode: https://www.linode.com/speedtest
* Vultr: https://www.vultr.com/faq/#downloadspeedtests

## 引用

* 项目基于[https://github.com/huifenqi/django-project-skeleton](https://github.com/huifenqi/django-project-skeleton)构建
* 部分前端代码来自于[http://www.cloudping.info/](http://www.cloudping.info/)
