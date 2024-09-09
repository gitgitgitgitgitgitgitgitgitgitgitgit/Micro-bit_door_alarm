
import radio
import basic
import Dimension

# micro:python script to send data from the senser micro:bit through radio to the receiver micro:bit

# set the radio group to 10
radio.set_group(10)


# funtion to send data via radio
def on_forever():
	# check if the magnetic force is less than 200. 
    if input.magnetic_force(Dimension.STRENGTH) < 200:
        #send the message "o" (meaning open) to the receiver micro:bit
        radio.send_string("o")
    # this else runs if the magnetic force is greater than 200    
    else:
        #send the message "c" (meaning closed) to the receiver micro:bit.
        radio.send_string("c")
    # wait for 2 seconds
    basic.pause(2000)

# run the on_forever function forever    
basic.forever(on_forever)
