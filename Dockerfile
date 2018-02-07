FROM python:3
WORKDIR /
RUN pip3 install paho-mqtt flask requests
EXPOSE 80
COPY currentcostserver.py /
CMD ["/currentcostserver.py"]
