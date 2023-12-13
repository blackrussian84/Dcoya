<p align="center">
  <i align="center">Creating a Static Web page with Devops 🦸 magic 🪄 and Security in Mind 🚀</i>
</p>

<p align="center">
<i align="center">Devops Challenge</i>
</p>
<h4 align="center">
    <img src="https://wallpapercave.com/uwp/uwp4109137.png" alt="continuous integration" style="height: 700px;">
  </a>
</h4>

  
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

![deploymentyml](https://github.com/blackrussian84/Dcoya/assets/61284544/936cc9e3-ae4a-4e79-8e6d-9b18041f7190)

service.yml

![serviceyml](https://github.com/blackrussian84/Dcoya/assets/61284544/c4c35ebd-4032-4f9f-b168-afb135e70095)

ingress.yml

![ingressyml](https://github.com/blackrussian84/Dcoya/assets/61284544/3ad51484-9d9f-403d-8f79-74f6b0e5bf43)


```bash
Kubectl apply -f deployment.yml.....
```


### Testing stage:
Python script was created with interactive mode and default parameters:
> The script ask you for domain, port and the cert path

![Screenshot from 2023-12-13 01-35-28](https://github.com/blackrussian84/Dcoya/assets/61284544/4b4f1e80-4d68-4efa-9384-79501560f4ac)


</details>
<details open>
  Lens Kubernetes IDE images of successful deployment:
<summary>
</summary> <br />

![Screenshot from 2023-12-13 02-40-02](https://github.com/blackrussian84/Dcoya/assets/61284544/68299411-f55c-4247-af61-4ccfb62d2e5c)

![Screenshot from 2023-12-13 02-43-21](https://github.com/blackrussian84/Dcoya/assets/61284544/c77fc84f-0a93-4e58-9d9f-eff0907d5e39)

![Screenshot from 2023-12-13 02-45-32](https://github.com/blackrussian84/Dcoya/assets/61284544/b7217f81-da03-4368-9459-4155e98ad0dc)

> Docker hub 

![Screenshot from 2023-11-21 21-09-53](https://github.com/blackrussian84/Dcoya/assets/61284544/7e515b57-86bb-49a0-b480-e16e48f376e0)

