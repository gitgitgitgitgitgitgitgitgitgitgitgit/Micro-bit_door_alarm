#This is then python scrip that runs on the Raspberry Pi.
#It reads the data from the serial port and sends a message to the telegram bot when the door is opened or closed.

# Import the necessary libraries
from telegram import Bot
import time
import serial

# sets the necessary variables
chat_id = 'replace with your chat id'
bot_token = "replace with your bot token"
message = "No data received from the sensor. Please check the connection."
bot = Bot(token=bot_token)

# Set up the serial port
serialPort = 'COM4'
baudRate = 115200
ser = serial.Serial(serialPort, baudRate, timeout=1)

# Give the serial port some time to establish
time.sleep(2)

# initialize the line variable
line = "x"

# Function to send a message to the telegram bot
def send_message(message):
      bot.send_message(chat_id=chat_id, text=message)


# Main loop to read the data from the serial port
while True:
	# Read the data from the serial port
        line = ser.readline().decode('utf-8').rstrip()
        # Check if the door is open or closed and calls the send_message function with the correct message
        if line == "o":
          message = "Your door is open."
          send_message(message)
        elif line == "c":
          message = "Your door is closed."
          send_message(message)
        
        
       
    
