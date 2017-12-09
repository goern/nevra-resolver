FROM registry.fedoraproject.org/fedora:27

WORKDIR /opt/redhat/thoth/nevra-resolver
EXPOSE 8080

COPY . /opt/redhat/thoth/nevra-resolver

RUN pip3 install -r requirements.txt

CMD ./app.py