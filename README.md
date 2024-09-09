This project leverages two micro:bits, a magnet, and a computer to send Telegram alerts when a door is opened or closed. The first micro:bit detects the strength of the electromagnetic field from the magnet placed on the door. When the door is opened or closed, this change in the magnetic field is sensed and a signal is sent to the second micro:bit. The second micro:bit communicates with a computer via serial, and the computer then uses Telegram's API to send a message alerting you of the door's status.

To set up the Telegram bot for this project, follow this guide to get your chat ID and Bot token: https://core.telegram.org/bots#how-do-i-create-a-bot
Remember to change your chat ID, and Bot token in computer.py. 
