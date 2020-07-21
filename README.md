# [Cloud Ping](http://cloudping.bastionhost.org/en/) &nbsp; [![Tweet](https://img.shields.io/twitter/url/http/shields.io.svg?style=social)](https://twitter.com/intent/tweet?text=This%20site%20allows%20you%20to%20perform%20an%20HTTP%20ping%20to%20measure%20the%20network%20latency%20from%20your%20browser%20to%20the%20various%20cloud%20data%20centers%20around%20the%20world.&url=http://cloudping.bastionhost.org/en/&via=github&hashtags=cloudping,cloud,latency,aws,azure,aliyun,developers)

[![Price](https://img.shields.io/badge/price-FREE-0098f7.svg)](https://github.com/bastionhost/cloudping/blob/master/LICENSE) &nbsp; [![Build Status](https://travis-ci.org/bastionhost/cloudping.png?branch=master)](https://travis-ci.org/bastionhost/cloudping)

This site allows you to perform an HTTP ping to measure the network latency from your browser to the various cloud data centers around the world.

![demo](./media/screenshot.png)

Visit http://cloudping.bastionhost.org/ for all clouds!

This project has the following basic apps:

* ping - the core app which implement the main logic.

## Installation

To set up a development environment quickly, install Python 2.x first. It
comes with virtualenv built-in. so create a virtual environment with:

`mkvirtualenv cloudping`

Install dependencies:

`pip install -r requirements.txt`

Run server:

`python manage.py runserver --settings=cloudping.settings.dev`

## Cloud endpoints

* AWS: http://ec2-reachability.amazonaws.com/
* Microsoft Azure: https://azure.microsoft.com/zh-cn/regions/
* Aliyun: https://help.aliyun.com/document_detail/40654.html
* Google Cloud: https://cloud.google.com/compute/docs/regions-zones/
* Tencent Cloud: https://cloud.tencent.com/document/product/213/6091
* Baidu Cloud: https://cloud.baidu.com/doc/BOS/S3.html#.E6.9C.8D.E5.8A.A1.E5.9F.9F.E5.90.8D
* Huawei Cloud: https://support.huaweicloud.com/obs/index.html
* Ksyun: https://docs.ksyun.com/directories/1782
* Qiniu Cloud: https://developer.qiniu.com/kodo/manual/1671/region-endpoint
* Qing Cloud: https://docs.qingcloud.com/qingstor/api/common/overview.html#地址构成
* UCloud: https://docs.ucloud.cn/api/summary/regionlist
* MOS: https://www.mtyun.com/doc/products/manage/Region/index
* Digital Ocean: http://speedtest-nyc1.digitalocean.com/
* Linode: https://www.linode.com/speedtest
* Vultr: https://www.vultr.com/faq/#downloadspeedtests

## Refs

* Project generated by [https://github.com/huifenqi/django-project-skeleton](https://github.com/huifenqi/django-project-skeleton)
* Some js code comes from [http://www.cloudping.info/](http://www.cloudping.info/)
