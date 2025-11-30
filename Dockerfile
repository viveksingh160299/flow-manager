FROM python:3.14.0
WORKDIR /app
COPY . .

RUN apt-get update && \
    apt-get install -y vim && \
    apt-get install -y sudo

ENV HOST='host.docker.internal'
ENV DATABASE='flow_manager_db'
ENV USER='postgres'
ENV PASSWORD='postgres'
ENV PORT='7777'
ENV AUTH_SECRET='14cf990eae3df0756bc23b48be5d5daa0ec3e40cee2f6306d708d22e0f340c0a14a74b3fe89e7abff912fba31d88f0da728ded4e99ab53688d29a2b5d703407214d25e1d26c6af52a5e889aa1d31c673d032948c7b0801060bc3939a8eb88b46098796e77c39a7c7a8fa1ae57f7ca7d6ce0bfdd2d46aafe011fcd7f1e66143d9'

RUN pip install -r requirements.txt