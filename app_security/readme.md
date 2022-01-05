- Установите Bitwarden плагин для браузера. Зарегистрируйтесь и сохраните несколько паролей.

```
https://ibb.co/ySdGqPM
```

- Установите Google authenticator на мобильный телефон. Настройте вход в Bitwarden акаунт через Google authenticator OTP.

```
https://ibb.co/Rp1wkcW
```

- Установите apache2, сгенерируйте самоподписанный сертификат, настройте тестовый сайт для работы по HTTPS.

```
sudo apt install apache2
cd /etc/apache2
sudo mkdir certs
sudo openssl req -new -x509 -days 1461 -nodes -out cert.pem -keyout cert.key -subj "/C=RU/ST=SPb/L=SPb/O=Global Security/OU=IT Department/CN=test.dmosk.local/CN=test"
sudo a2enmod ssl
systemctl restart apache2
sudo vim sites-enabled/site
sudo apachectl configtest
sudo apache graceful
sudo wget localhost:443
cat index.html
```

- Проверьте на TLS уязвимости произвольный сайт в интернете.

```
https://www.sslshopper.com/ssl-checker.html#hostname=www.google.com
```

- Установите на Ubuntu ssh сервер, сгенерируйте новый приватный ключ. Скопируйте свой публичный ключ на другой сервер. Подключитесь к серверу по SSH-ключу.

```
On server (vagrant):
sudo apt install openssh-server
sudo systemctl enable ssh
On client:
ssh-keygen (enter, enter, enter)
ssh-copy-id -p 2222 vagrant@127.0.0.1
ssh -p 2222 vagrant@127.0.0.1
```

- Переименуйте файлы ключей из задания 5. Настройте файл конфигурации SSH клиента, так чтобы вход на удаленный сервер осуществлялся по имени сервера.
```
sudo vim ~/.ssh/config
```
config:
```
Host vagrant
        HostName 127.0.0.1
        User vagrant
        Port 2222
        IdentityFile ~/.ssh/custom_key
```
```
ssh-keygen
name: custom_key
ssh-copy-id -i ./custom_key -p 2222 vagrant@127.0.0.1
ssh vagrant
```

- Соберите дамп трафика утилитой tcpdump в формате pcap, 100 пакетов. Откройте файл pcap в Wireshark.
```
https://ibb.co/4MYfsLT
```
