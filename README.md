<p align="center">
  <i align="center">Creating a Static Web page with Devops 🦸 magic 🪄 and Security in Mind 🚀</i>
</p>
<p align="center">
<i align="center">Devops Challenge</i>
</p>
<h4 align="center">
    <img src="https://github.com/blackrussian84/Dcoya/assets/61284544/3abddffc-165b-4945-bdfe-e90355d6fcf5" alt="continuous integration" style="height: 700px;">
  </a>
</h4>


![Screenshot from 2023-12-13 02-55-07](https://github.com/blackrussian84/Dcoya/assets/61284544/3abddffc-165b-4945-bdfe-e90355d6fcf5)


## 

  

## 
Tools Used  

- [GET Minikube](https://minikube.sigs.k8s.io/docs/start/)
- [GET kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/) 
- [GET docker](https://docs.docker.com/get-docker/)
- [GET Lens](https://k8slens.dev/) 


###
Creating index Html with the JS 🧞

 ![Screenshot from 2023-12-12 22-38-59](https://github.com/blackrussian84/Dcoya/assets/61284544/924156d6-4fa9-49ee-9cfb-d499d413c842)

 POC WORKED 😻

</details>
<details open>
<summary>
The Html + JS code
</summary> <br />

```html
<!DOCTYPE html>
<html>
<head>
    <title>Machine Info</title>
    <script>
        function displayInfo() {
            document.getElementById('machineName').textContent = 'Machine Name: ' + '__MACHINE_NAME__';
            document.getElementById('dateTime').textContent = 'Date and Time: ' + new Date();
        }
    </script>
</head>
<body onload="displayInfo()">
    <h1>Machine Info</h1>
    <p id="machineName"></p>
    <p id="dateTime"></p>
</body>
</html>
```

> ⛔ JavaScript running in a browser cannot directly access environment variables for security reasons so 
> server-side code was nedded to be created to inject the environment variable into our HTML 🔒

```shell
#!/bin/sh
# Replace the placeholder with the actual machine name
# using the command: [docker run -p 8008:80 -e MACHINE_NAME=JenyaMachine -d my-app2:latest]
## The change will be effective with each run of the Docker, as opposed to building the Docker in the advanced project. 
sed -i "s/__MACHINE_NAME__/$MACHINE_NAME/g" /usr/share/nginx/html/index.html
# Start Nginx
nginx -g 'daemon off;'
```

## Dockerfiles:



## Then I decided to shift gears!

![Screenshot from 2023-12-13 02-27-22](https://github.com/blackrussian84/Dcoya/assets/61284544/1e7141cd-7ff7-4ac6-a763-4c80f4f5a7be)


> The agenda was to create static content with a 'cute look',
> that will be served by [NGINX].


1.create a project dir and cd into it:
```bash
npx create-react-app my-app
# Modify, create a production-ready artifact with static content and logic, then pass it to the Nginx Dockerfile later on:
npm run build
```
Creating the self signed certificate:
```bash
 openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout tls.key -out tls.crt -config openssl.cnf -extensions 'v3_req'
```
Creating the volumes to pass the crt and key securly:
```bash
docker volume create ssl_cert
docker volume create ssl_private
```
Bulding and run the Dockerfile :
```bash
docker build -t myapp .
docker run -p 8008:80 -e MACHINE_NAME=JenyaMachine -d my-app2:latest        # in the POC case above
docker run -v cat_ssl_certs:/etc/ssl/certs -v cat_ssl_private:/etc/ssl/private -d -it -p 443:443 cats:latest     #  secure way with mounted volumes
# 
```
Taging the imag and push it to docker-hub
```bash
docker tag mydocker docker.io/blackrussian84/mydocker:latest
docker push docker.io/blackrussian84/mydocker:latest
```

The k8s deployment was created with yml files:

#The app deployed to chosen namespace.
#ingress contraller was deployed.
#SSL termination was implemented on the ingress level, the dockerfile and the service was configured accordinly.
#kubernetes secret was created and injected via the deployment/ingress
deployment.yml
```bash
apiVersion: apps/v1
kind: Deployment
metadata:
  name: cats-app
  namespace: cats
  labels:
    app: cats-app
spec:
  replicas: 1
  selector:
    matchLabels:
      app: cats-app
  template:
    metadata:
      labels:
        app: cats-app
    spec:
      containers:
      - name: cats-app
        resources:
          limits:
            cpu: "0.5"
            memory: "512Mi"
          requests:
            cpu: "0.2"
            memory: "256Mi"
        image: docker.io/blackrussian84/catshttp:latest
        ports:
        - containerPort: 443
        - containerPort: 80    
        volumeMounts:
        - name: tls
          mountPath: "/etc/ssl/certs/tls.crt"
          subPath: "tls.crt"
          readOnly: true
        - name: tls
          mountPath: "/etc/ssl/private/tls.key"
          subPath: "tls.key"
          readOnly: true
      volumes:
      - name: tls
        secret:
          secretName: catsecret   
```


service.yml
```bash
apiVersion: v1
kind: Service
metadata:
  namespace: cats
  name: cats-app-service
  labels:
    app: cats-app
spec:
  selector:
    app: cats-app
  ports:
    - name: http
      protocol: TCP
      port: 80
      targetPort: 80
  type: NodePort
   
```


ingress.yml

```bash
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  namespace: cats
  name: cats-app-ingress-https
spec:
  tls:
  - hosts:
    - dev.cats.com
    secretName: catsecret
  rules:
  - host: dev.cats.com
    http:
      paths:
      - pathType: Prefix
        path: "/"
        backend:
          service:
            name: cats-app-service
            port:
              number: 80

```


```bash
Kubectl apply -f deployment.yml.....ingre......ser....
```


### Testing stage:
Python script was created with interactive mode and default parameters:
> The script ask you for domain, port and the cert path

![Screenshot from 2023-12-13 01-35-28](https://github.com/blackrussian84/Dcoya/assets/61284544/4b4f1e80-4d68-4efa-9384-79501560f4ac)

### Screenshoots of success

</details>
<details open>
  Lens Kubernetes IDE images of successful deployment:
<summary>
</summary>  

![Screenshot from 2023-12-13 02-40-02](https://github.com/blackrussian84/Dcoya/assets/61284544/68299411-f55c-4247-af61-4ccfb62d2e5c)

![Screenshot from 2023-12-13 02-43-21](https://github.com/blackrussian84/Dcoya/assets/61284544/c77fc84f-0a93-4e58-9d9f-eff0907d5e39)

![Screenshot from 2023-12-13 02-45-32](https://github.com/blackrussian84/Dcoya/assets/61284544/b7217f81-da03-4368-9459-4155e98ad0dc)

> Docker hub 

![dockerhub](https://github.com/blackrussian84/Dcoya/assets/61284544/e5583684-c3ce-4a35-8264-3ecd18f0fc53)

![Screenshot from 2023-12-12 22-33-44](https://github.com/blackrussian84/Dcoya/assets/61284544/60f044b6-93d2-45e9-b3fe-646e9597ed70)


