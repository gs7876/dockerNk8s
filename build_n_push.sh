cd app
sudo docker build --tag gs7876-sample-api .
docker tag gs7876-sample-api gs7876/sample-api:1.0.0
docker push gs7876/sample-api:1.0.0