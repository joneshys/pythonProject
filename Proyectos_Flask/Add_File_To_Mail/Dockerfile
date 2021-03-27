FROM centos:7
RUN yum install python3 -y && pip3 install --upgrade pip
WORKDIR /app
COPY . /app
RUN mkdir /root/.aws
COPY config /root/.aws
COPY credentials /root/.aws
RUN pip3 --no-cache-dir install -r requirements.txt
CMD ["python3", "add_file_to_mail.py"]