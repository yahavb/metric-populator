FROM ubuntu:latest
RUN apt-get update -y --fix-missing
RUN apt-get install -y net-tools curl vim
RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

RUN pip install requests numpy boto3

ADD report_current_gs_count.py /report_current_gs_count.py
RUN chmod a+x /report_current_gs_count.py
CMD /report_current_gs_count.py
