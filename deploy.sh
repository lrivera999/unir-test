#!bin/bash
cd $1
docker build -t calculator-app .
docker network create calc-test-api || true

docker run -d --volume `pwd`:/calc-test-api \
--name apiserver --network calc-test-api \
--env PYTHONPATH=/opt/calc --env FLASK_APP=app/api.py \
-p 5000:5000 \
-w /opt/calc calculator-app:latest flask run --host=0.0.0.0 || true