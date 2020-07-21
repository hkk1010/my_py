#!/usr/bin/python3
# coding:utf-8

from elasticsearch import Elasticsearch
import socket
from prometheus_client import CollectorRegistry, Gauge, push_to_gateway,Counter
import time
import  logging
import datetime

def calculate_electricty_count(url,job_name):
    logging.basicConfig(level=logging.DEBUG,  # 控制台打印的日志级别
                        filename='new.log',
                        filemode='a',
                        format=
                        '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
                        )
    es = Elasticsearch(['192.168.3.96:9200'], timeout=3600)
    struct_time = time.localtime(time.time())
    Today = time.strftime("%Y.%m.%d", struct_time)
    pre_day = (datetime.datetime.now() - datetime.timedelta(days = 1))
    yestoday = pre_day.strftime("%Y.%m.%d")
    try:
        if es.indices.exists(index='logstash-job-executor-'+ Today) == True :
            query_count = es.count(index='logstash-job-executor-' + Today,
                                   q='HANDLER_NAME: com.ll.job.lljobexecutor.jobhandler.CalculateElectricStatisticsHandler')
            running_count = query_count['count']
            post_Calculate_data(url,job_name,running_count)
            logging.info('电费统计job运行0k')
        else:
            query_count = es.count(index='logstash-job-executor-' + yestoday,
                               q='HANDLER_NAME: com.ll.job.lljobexecutor.jobhandler.CalculateElectricStatisticsHandler')
            running_count = query_count['count']
            post_Calculate_data(url, job_name, running_count)
            logging.info('电费统计job运行0k')
    except Exception as ex:
            logging.error("电费统计job出现异常:" + ex)
            #print(ex)

def post_Calculate_data(url,job_name,running_count):
    hostname = socket.gethostname()
    registry = CollectorRegistry()
    g = Gauge('Calculate_electricity', '', ['cluster', 'type', 'job_name', 'course','instance'],
              registry=registry)
    g.labels('product', 'job', job_name, 'post_Calculate_data',hostname).set(running_count)
    push_to_gateway(url, job='Calculate_electricity', registry=registry)

if __name__=="__main__":
    #url = "http://pushgateway.feiersmart.local:9091"
    job_name="ll-job-executor"
    url = "http://192.168.6.216:9091"
    calculate_electricty_count(url,job_name)
