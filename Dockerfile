FROM python:3.12-slim

WORKDIR /workspace
ENV HOME=/workspace

COPY requirements.txt /workspace
RUN pip install -r requirements.txt

ADD . /workspace

RUN chown -R 42420:42420 /workspace



EXPOSE 8080

ENTRYPOINT ["uvicorn"]

CMD ["main:app", "--host", "0.0.0.0", "--port", "8080"]


# this docker image work for OVH CLOUD AI DEPLOY