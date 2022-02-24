cd app
sudo docker build --tag gs7876-sample-api .
docker tag gs7876-sample-api gs7876bksc/gs7876-repository:1.0.0
docker push gs7876bksc/gs7876-repository:1.0.0

# tag name is gs7876-sample-api
# gs7876bksc/gs7876-repository is my repositary name
# 2.0.0 is version