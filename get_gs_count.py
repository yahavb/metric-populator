#!/opt/local/bin/python3
##!/usr/bin/python3


import boto3
import signal
import datetime
import time
import numpy as np
import os

#namespace=os.environ['NAMESPACE']
namespace='my-mmo-1'
#region=os.environ['REGION']
region='us-west-2'
#metric=os.environ['METRIC']
metric='num-active-gs'
metricid='metricid'

today = datetime.date.today()
one_day = datetime.timedelta(days=1)
yesterday = today - one_day
tommorrow = today + one_day

client = boto3.client('cloudwatch',region_name='us-west-2')

def sigterm_handler(_signo, _stack_frame):
    print ("going down")
    sys.exit(0)

def get_metric_by_region(region,namespace,metric,metricid):
  response = client.get_metric_data(
    MetricDataQueries=[
        {
            'Id':metricid,
            'MetricStat': {
                'Metric': {
                    'Namespace': namespace,
                    'MetricName': metric,
                    'Dimensions': [
                        {
                            'Name':'region',
                            'Value': region
                        },
                    ]
                },
                'Period': 1,
                'Stat': 'SampleCount',
                'Unit': 'Count'
            },
        },
    ],
    StartTime=yesterday.ctime(),
    #EndTime=today.ctime()
    EndTime=tommorrow.ctime()
  )
  return response

if __name__ == '__main__':
  res=get_metric_by_region(region,namespace,metric,metricid)
  print(today.ctime(),yesterday.ctime())
  print(tommorrow.ctime())
  print(res)
