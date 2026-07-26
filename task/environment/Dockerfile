FROM python:3.12-alpine

WORKDIR /workspace

RUN apk add --no-cache bash ca-certificates

COPY . /workspace

RUN pip install --no-cache-dir pytest

CMD ["/bin/bash"]
