# Telegram Bot
This dockerized Python code employs a simple API and the Telegram Bot API to provide a service that enables individuals to determine whether their passwords have been compromised.

## Usage
To set up the bot, start by running the `telegram-bot-setup.sh` file. This script will configure a webhook on the Telegram servers to receive messages from the bot as soon as they are sent. The Dockerfile included in this repository has also been modified to include the HTTP API token for the Telegram bot.

To run the Telegram bot container, execute the following command: `sudo docker-compose up -d`.

## Client comands
|   Command    |  Response  |
|--------------|------------|
|   /start     |     Send me your password to cross check it over the xposedornot.com dataset to check whether your password has been already exposed       |
|   Password   |      [Your password has been repeated in password breaches this many times: NUM]/Your password is potentially safe.       |
