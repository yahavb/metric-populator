#!/usr/bin/python3

##!/opt/local/bin/python3

import boto3
import signal
import time
import numpy as np
import os

namespace=os.environ['NAMESPACE']
region=os.environ['REGION']
metric=os.environ['METRIC']
freq=os.environ['FREQ']
scalevalue=os.environ['SCALEVALUE']

client = boto3.client('cloudwatch',region_name='us-west-2')


i=0

def sigterm_handler(_signo, _stack_frame):
    print ("going down")
    sys.exit(0)

def populate_metric_by_region(region,namespace,metric,value):
  response = client.put_metric_data(
    Namespace=namespace,
    MetricData=[
        {
            'MetricName': metric,
            'Dimensions': [
                {
                    'Name': 'region',
                    'Value': region 
                },
            ],
            'Value': value,
        },
    ]
 )


if __name__ == '__main__':
  while True:
    i=i+1
    A = np.sin(i*10E2)*10E1
    if (A>0):
      B=A
    else:
      B=-1*A 
    sample=int(B)/int(scalevalue)
    print("region:"+region+",namespace:"+namespace+",metric:"+metric+",sample:"+str(sample))
    populate_metric_by_region(region,namespace,metric,sample)
    time.sleep(int(freq))
