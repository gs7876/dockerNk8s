FROM python:alpine3.7

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

RUN apk --no-cache add curl

EXPOSE 5001

ENTRYPOINT [ "python" ]

CMD [ "sampleapi.py" ]
