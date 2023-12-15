# This is a sample Python script
import math
import random
import time

import pyaudio
import turtle
import numpy as np
#to import packages such as numpy and pyaudio and turtle, I had to download them. I went to the top bar, clicked on View --> tool windows --> pythonpackages --> add package

#code I was using as inspiration : https://editor.p5js.org/mwong23/full/910v_Nx4W

# creating screen for drawing
screen = turtle.Screen()
my_turtle = turtle.Turtle()
screen.colormode(255)


#reference https://youtu.be/SlL7VYYaTGA?si=s8uyzonjUfWxAomP
CHUNK = 1024
# paInt16 is the type of sound data it is
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100


# opening the audio stream
p = pyaudio.PyAudio()
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)
print("* recording")


def drawing_audio(vol_dat):

    #checks if volume is a number, if its not a number it quits the function
    # isnan reference: https://www.w3schools.com/python/ref_math_isnan.asp#:~:text=isnan()%20method%20checks%20whether,NaN%2C%20otherwise%20it%20returns%20False.
    if math.isnan(vol_dat):
        return
    vol_a = int(vol_dat)



    # changing color based on volume
    # color = (vol_a * 255, 0 + vol_a * 255, 40)
    r_color = min(vol_a * random.randint(0,15), 255)
    b_color = min(vol_a * random.randint(0,15) + random.randint(0,25), 255)
    g_color = min(vol_a * random.randint(0,15), 255)

    my_turtle.fillcolor(r_color, g_color, b_color)
    my_turtle.begin_fill()

    # Draw an ellipse with size based on volume
    my_turtle.setposition(0,0)
    my_turtle.penup()
    # turn a number between 10 and 90 and set it to be named degrees
    degrees = random.randint(10,90)
    my_turtle.forward(80)
    # moves left however the amount of degrees is set
    my_turtle.left(degrees)
    my_turtle.pendown()
    # using the volume to get the size of the circle/ the radius
    size = vol_a *2 + 5
    my_turtle.circle(size / 2+20)
    my_turtle.end_fill()

    # Update the display
    turtle.update()


def get_volume(wavefile_temp):


    #reference
    # Convert the binary audio data to a NumPy array
    audio_array = np.frombuffer(wavefile_temp, dtype=np.int16)
    if audio_array.size == 0:
        return 0
    # Calculate the RMS (Root Mean Square) of the audio data to get the volume
    rms = np.sqrt(np.mean(np.square(audio_array)))
    return rms

# runs 50 times
for i in range(50):
    data = stream.read(CHUNK, exception_on_overflow=False)
    # frames.append(data)
    volume = get_volume(data)
    drawing_audio(volume)
    print(volume)
    # waiting period between drawings
    time.sleep(.5)

print("* done recording")



stream.stop_stream()
stream.close()
p.terminate()
screen.exitonclick()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
