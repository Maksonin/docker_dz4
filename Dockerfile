FROM ubuntu
RUN apt update && apt install -y python3 nginx
EXPOSE 8081
COPY hello.py /
CMD python3 /hello.py
