## 🌿 Ping Server
### Created by M20191

## ☀ Available Servers
* Minecraft Bedrock
* Minecraft Java

## 💻 Info get
* time_ping
* ip
* players
* max/players
* availability
* latency
* version/bunge
* description
* status

## 🛠 Downloading script and requirements in linux:
```console
wget "https://raw.githubusercontent.com/M20191/MSD-Z-Ultimate/'main'/scripts/ping_server/ping_server.py" && pip install mcstatus
```

## 🛠 Downloading script and requirements in Windows:
```console
Invoke-WebRequest -uri "https://raw.githubusercontent.com/M20191/MSD-Z-Ultimate/'main'/scripts/ping_server/ping_server.py" -OutFile ping_server.py -UseBasicParsing ; pip install mcstatus
```


## Args console
```
Ip address to consult data
-ip 
--host

Outfile to save ping data (optional)
-o
--outfile

```
## 🖥 How to run script file in Linux:
```console
python3 .\ping_server.py -ip mc.hypixel.net


```

## 🖥 How to run script file in Windows:
```console
python .\ping_server.py -ip mc.hypixel.net
```