# Important notes

### Install minicube

> curl -LO [https://storage.googleapis.com/minikube/releases/latest/minikube-darwin-amd64](https://storage.googleapis.com/minikube/releases/latest/minikube-darwin-amd64)

> sudo install minikube-darwin-amd64 /usr/local/bin/minikube

### Operate minicube

* > minikube start OR minikube start --cpus 6 --memory 8192
* > minikube stop
* > minikube delete
* > more /.kube/config
* > export KUBECONFIG=/.kube/config
* > minikube dashboard
* > minikube ssh
* > sudo vi /etc/systemd/network/[10-eth1.network](http://10-eth1.network) add DNS=8.8.8.8 under [Network]
* > sudo vi /etc/systemd/network/[20-dhcp.network](http://20-dhcp.network) add DNS=8.8.8.8 under [Network]
* > sudo systemctl restart systemd-networkd

### docker build image

> sudo docker build --tag gs7876-sample-api .

> docker tag gs7876-sample-api gs7876/sample-api:1.0.0

> docker push gs7876/sample-api:1.0.0

### docker run

docker run -p 8080:9090 gs7876-sample-api

> 8080 is local port to access http://0.0.0.0:8080/health/full

> 9090 is comntainer port

| Flag value                        | Description                                                                                                                                     |
| --------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| `-p 8080:80`                    | Map TCP port 80 in the container to port 8080 on the Docker host.                                                                               |
| `-p 192.168.1.100:8080:80`      | Map TCP port 80 in the container to port 8080 on the Docker host for connections to host IP 192.168.1.100.                                      |
| `-p 8080:80/udp`                | Map UDP port 80 in the container to port 8080 on the Docker host.                                                                               |
| `-p 8080:80/tcp -p 8080:80/udp` | Map TCP port 80 in the container to TCP port 8080 on the Docker host, and map UDP port 80 in the container to UDP port 8080 on the Docker host. |
