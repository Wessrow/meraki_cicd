FROM ubuntu:18.04

ENV TESTVAR=blahblah

RUN "apt-get update -y && apt-get install -y python3"

ENTRYPOINT ["python3"]

RUN meraki_sdk.py
