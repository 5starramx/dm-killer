<p align="center">
  <img src="https://imagedelivery.net/95QNzrEeP7RU5l5WdbyrKw/01531dee-c00f-4712-5975-16487c0b3f00/shopitem"><br>
  <img src="https://img.shields.io/github/stars/despk/dm-killer?style=for-the-badge&logo=appveyor">
  <img src="https://img.shields.io/github/forks/despk/dm-killer?style=for-the-badge&logo=appveyor">
  </p>

# Discord Mass DM Killer
**DM-KILLER** is a Multi-threaded Discord Self-Bot primarily used for mass messaging users on Discord. It has numerous other quality features to enhance the user experience and allowing the user to target the most users. 

## **Features** :
### Mass Messaging
- Mass DM Advertisement 
- Server Checker
### Other Features
- Multiple Captcha APIs supported
- Supports token format
- Compatible with all major OS and Architectures
- Proxyless 
- Supports HTTP(s), SOCKS5 and SOCKS4 proxies
- Free & Open source
- Emulates Discord's requests to a very high accuracy to prevent detection
- Multi-threaded using Light-weight Goroutines supporting thousands of concurrent accounts
- Can Receieve messages during mass DM
- Can ping user
### Preview
<p align="center">
  <img src="https://i.imgur.com/IJc65Dn.png">
</p>

 
## Basic Usage
1) [Download Source](https://github.com/despk/dm-killer/archive/refs/heads/main.zip)
2) Extract to desktop
3) Configure your config.json
4) If you already have memberids to DM, put them in `\data\memberids.txt` or obtain them from [Scraping](https://github.com/despk/discord-id-scraper/archive/refs/heads/main.zip)
5) Put Proxy in `config.json`. The format is `IP:Port` or `User:pass@IP:Port` if your proxies have a user-pass authentication. 
6) Enter your message(s) in `\data\message.txt` file.

## Building from source
1) Download and install [Python](https://www.python.org/downloads/) and verify your installation
2) Open a terminal window/command prompt in the directory of the source code and type `pythom dm.py` (Just do this after proceeding with Basic Usage)

## Using Captcha APIs
Captcha Solving APIs were introduced to DM-KILLER on 8th February 2022 when Discord mandated Captchas for joining servers on some tokens they deemed untrustworthy. The supported Captcha APIs right now are capmonster.cloud and anti-captcha.com 
You can register an account there, load some balance and copy your Captcha API Key to config. Make sure to specify the service you're using as well. It is extremely inexpensive and can join thousands of accounts in a couple USD. If there is an error with the captcha APIs, You will get an error code. You can look it up on their documentation [here](https://anti-captcha.com/apidoc/errors)

### Example configuration
```json
{
    "proxy": "proxy here IP:Port or User:pass@IP:Port",
    "timeout_min": 60,
    "timeout_max": 120,
    "captcha_type": "capmonster/anticaptcha/2captcha",
    "capmonster_apikey": "",
    "anticaptcha_apikey": "",
    "twocaptcha_apikey": "",
    "server_id": "server id for the tool to check if the token is on the server before sending a message"
}
```
This is the config I'd use, with ofcourse the offset calculated accordingly.


## Credits
- [Created by Effe](https://t.me/effe_discord) && [Cracked/Updated by me :)](https://github.com/despk/)
