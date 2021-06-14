FROM python:3.8.10-alpine

ENV MERAKI_API_TOKEN="PLACEHOLDER - Run container with -e MERAKI_API_TOKEN=<MerakiAPIToken>"

WORKDIR /app/

COPY . /app/

RUN pip install -r requirements.txt

ENTRYPOINT ["python3"]

CMD ["meraki_sdk.py"]
