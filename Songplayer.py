from tkinter.constants import N
from gi.repository import Notify
from playsound import *
import tkinter as tk 
import random

usr = input("What is your Username?")

songnumbers = int(input("You should have your songs labeled by number in assending order. \n How many songs do you have?"))
while True:
    songnumber = random.randint(1,songnumbers)
    Notify.init("Jammer")
    Notify.Notification.new("New song Playing!").show()

    str(songnumbers)

    playsound('/home/'+ usr +'/Music/' + str(songnumbers) + '.mp3')

