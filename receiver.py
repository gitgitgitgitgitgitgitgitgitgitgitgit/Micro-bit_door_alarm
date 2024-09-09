# micropython script to 
import radio
import serial
import basic

# micro:python script to receive data from the senser micro:bit through radio and send it via serial to the Raspberry Pi

# set the radio group to 10
radio.set_group(10)


# funtion to get data and send it via serial
def on_received_string_deprecated(receivedString):
    global sent_message
    # check if the door is open, also checks the last sent message to avoid sending the same message multiple times
    if receivedString == "o" and sent_message == 0:
        #write to the serial port
        serial.write_line("o")
        #change the sent_message variable to avoid sending the same message multiple times
        sent_message = 1
    # check if the door is closed, also checks the last sent message to avoid sending the same message multiple times
    elif receivedString == "c" and sent_message == 1:
        #write to the serial port
        serial.write_line("c")
        #change the sent_message variable to avoid sending the same message multiple times
        sent_message = 0
    # wait for 500ms
    basic.pause(500)

radio.on_received_string_deprecated(on_received_string_deprecated)

