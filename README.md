# Important notes

**docker build image**

> sudo docker build --tag gs7876-sample-api .

> docker tag gs7876-sample-api gs7876/sample-api:1.0.0

> docker push gs7876/sample-api:1.0.0

**docker run**

docker run -p 8080:9090 gs7876-sample-api

> 8080 is local port to access http://0.0.0.0:8080/health/full 

> 9090 is comntainer port

| Flag value                        | Description                                                                                                                                     |
| --------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| `-p 8080:80`                    | Map TCP port 80 in the container to port 8080 on the Docker host.                                                                               |
| `-p 192.168.1.100:8080:80`      | Map TCP port 80 in the container to port 8080 on the Docker host for connections to host IP 192.168.1.100.                                      |
| `-p 8080:80/udp`                | Map UDP port 80 in the container to port 8080 on the Docker host.                                                                               |
| `-p 8080:80/tcp -p 8080:80/udp` | Map TCP port 80 in the container to TCP port 8080 on the Docker host, and map UDP port 80 in the container to UDP port 8080 on the Docker host. |
