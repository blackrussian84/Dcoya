<p align="center">
  <i align="center">Static Web page with Devops 🦸 magic 🪄 and Security in Mind 🚀</i>
</p>


<h4 align="center">
  <a href="https://github.com/amplication/amplication/actions/workflows/ci.yml">
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


 POC WORKED 😻
 ![Screenshot from 2023-12-12 22-38-59](https://github.com/blackrussian84/Dcoya/assets/61284544/924156d6-4fa9-49ee-9cfb-d499d413c842)


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
sed -i "s/__MACHINE_NAME__/$MACHINE_NAME/g" /usr/share/nginx/html/index.html
# Start Nginx
nginx -g 'daemon off;'
```


## Then i desided to  shift gear 🐞
> The agenda was to create static content with cute look that will be served by the [NGINX] using React lib.
> so i ran

1.create a project dir and cd into it:
```bash
npx create-react-app my-app
#change what need to be chang and create a production ready artifact of all the static content and logic that will be passed to the Dockerfile with nginx as content.
#using the command:
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
docker run -p 8008:80 -e MACHINE_NAME=JenyaMachine -d my-app2:latest                                                        # in the POC case above
docker run -v cat_ssl_certs:/etc/ssl/certs -v cat_ssl_private:/etc/ssl/private -d -it -p 443:443 cats:latest                # in secure way with mounted volumes
```



⛔🔒🐞🧞😻
both the client and server need to be started by the `npm run serve:[application]`
To be able to start development on Amplication, make sure that you have the following prerequisites installed:





## Latest Development Changes
```bash
python -m pip install git+https://github.com/anfederico/clairvoyant
```
> **Note**
> In order to run the Amplication client properly, both the client and server need to be started by the `npm run serve:[application]`
**BEFORE** you run the following steps make sure:
1. You have typescript installed locally on you machine ```npm install -g typescript```
2. You are using a supported node version (check `engines` `node` in the [package.json](./package.json))
3. You are using a supported npm version (check `engines` `npm` in the [package.json](./package.json))
4. You have `docker` installed and running on your machine
 
```python
from clairvoyant.engine import Backtest
import pandas as pd

features  = ["EMA", "SSO"]   # Financial indicators of choice
trainStart = 0               # Start of training period
trainEnd   = 700             # End of training period
testStart  = 701             # Start of testing period
testEnd    = 1000            # End of testing period
buyThreshold  = 0.65         # Confidence threshold for predicting buy (default = 0.65) 
sellThreshold = 0.65         # Confidence threshold for predicting sell (default = 0.65)
continuedTraining = False    # Continue training during testing period? (default = false)
```

