# monitoring_users_plex_bot
[![CI](https://github.com/soueuflavio/monitoring_users_plex_bot)

Monitoring PLEXPY and setup DOCKER Stop Containers the Downloads
### How it works

- When a movement is detected, the application records a video that is sent to your phone by the Telegram bot.  
- Once installed, the surveillance system is managed from your smartphone with [bot commands](#Bots-commands) from the Telegram app.  
- The system is started by a systemd service activated at boot time

### Prerequisites.

* Raspberry Pi Camera Module  
* PIR motion sensor module   
* 3 female-to-female jumper wires   
* [Tutorial for create your Telegram Bot](https://core.telegram.org/bots#3-how-do-i-create-a-bot)  
* After starting the bot on your smartphone, you must retrieve your chat_id at the following address:   
    * https://api.telegram.org/bot<token_id>/getUpdates

### Connect the PIR sensor

![image](img/pir-diagram.png)

## Setting up the camera hardware
```

```
After this action reboot the raspberry

## Setup
   
 * Open the `config.py` file and configure the TOKEN_ID and CHAT_ID variables with your token_id and your chat_id  
 ```
# Variable to configure
TOKEN_ID = 'Your token_id'
CHAT_ID = 'Your chat_id' 

# Variable that can be modified
VIDEO_TIME = 60  # duration of video recording in second

# Variable para Plexpy
tautulli_apikey = 'Yout api key by tautulli'
tautulli_url_port = 'Yout IP and PORT by tautulli'

# Variable para Docker Daemon, for access Docker`s API
docker_nas_url = 'Yout IP and PORT by DOCKER'   
```

### Installing 

Before installing set your token_id then:
```
sudo make install
```

### Bot's commands

* /command  : description command
  
### Details 		

  * By default `config.py` setup tautulli and docker daemon    		

  * It's possible to add other commands to the bot in `app.py` 
 
### Testing
 
```
make test
```

### Uninstall
 
```
sudo make uninstall
```

## Built With
