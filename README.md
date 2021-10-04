# Bitly url shortener

Input some URL to get a Bitly short link and forget about long URLs. 
The script allows you to shorten links using the [bitly](https://bitly.com) service, as well as get the number of clicks on the shortened link.

## How to install

- Go to [bitly](https://bitly.com), sign up and generate your token: settings -> api -> Generate token

- Download the project as .zip or clone the actual repository 

- Create a file .env and put inside 
```bash
BITLY_TOKEN=YOUR_TOKEN
```
- Python3 should be already installed. Then use pip (or pip3, if there is a conflict with Python2) to install dependencies:

```bash
$python pip install -r requirements.txt
```

```bash
$python python3 main.py "here is your long URL"
```

And that's it. You have got the bitly link. For example: [bit.ly/3ieEuGB](https://bit.ly/3ieEuGB)

## Project Goals

The code is written for educational purposes on online-course for web-developers [Devman](https://dvmn.org).