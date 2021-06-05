 # cd .\Dropbox\arduino\; python .\play_from_serial.py
from serial import Serial
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys
import datetime		
import time		
import rtmidi
import re 
import random
import os
from rtmidi.midiconstants import (ALL_NOTES_OFF, ALL_SOUND_OFF, BALANCE, BANK_SELECT_LSB,
                                  BANK_SELECT_MSB, BREATH_CONTROLLER, CHANNEL_PRESSURE,
                                  CHANNEL_VOLUME, CONTROL_CHANGE, DATA_ENTRY_LSB, DATA_ENTRY_MSB,
                                  END_OF_EXCLUSIVE, EXPRESSION_CONTROLLER, FOOT_CONTROLLER,
                                  LOCAL_CONTROL, MIDI_TIME_CODE, NOTE_OFF, NOTE_ON,
                                  NRPN_LSB, NRPN_MSB, PAN, PITCH_BEND, POLY_PRESSURE,
                                  PROGRAM_CHANGE, RESET_ALL_CONTROLLERS, RPN_LSB, RPN_MSB,
                                  SONG_POSITION_POINTER, SONG_SELECT, TIMING_CLOCK)
from collections import deque
from serial.tools.list_ports import comports
# importing the requests library 
# import requests 

# defining the api-endpoint 
# API_ENDPOINT = "http://localhost:9876/drumify"
API_ENDPOINT = "http://drumbot.glitch.me/drumify"


global midiout
threshold0 = 7
threshold1 = 7
threshold2 = 7
threshold3 = 7
thresholds=[threshold0,threshold1,threshold2,threshold3]
num_for_three_channels = 5
num_for_two_channels = 3
velocity = 50
delay = 500
duration = 1500
freq_check_settings = 1522250

class TimedNote:
  def __init__(self, note, time = 0, channel=None):
    self.time = time
    # self.time_on  for drumify
    self.note = note	
    self.channel = channel
  time = 0
  note = 0
  channel = 0
  time_off = 0




def channel_message(command, *data, ch=None):
  # """Send a MIDI channel mode message."""
  command = (command & 0xf0) | ((ch if ch else 1) - 1 & 0xf)
  msg = [command] + [value & 0x7f for value in data]
  return msg



def playnote(n): 
    note_on = channel_message(NOTE_ON, n + 24, 52, ch = 1)
    note_on2 = channel_message(NOTE_ON, n + 32, 52, ch = 2)
    # note_on2 = [0x90, n + 32, 52]
    # note_off = [0x80, n + 24, 0]
    # note_off2 = [0x80, n + 32, 0]
    note_off = channel_message(NOTE_OFF, n + 24, 0, ch = 1)
    note_off2 = channel_message(NOTE_OFF, n + 32, 0, ch = 2)
    midiout.send_message(note_on)
    print("first note")
    print(note_on)
    time.sleep(1.25) 
    midiout.send_message(note_on2)
    time.sleep(1.5) 
    midiout.send_message(note_off)
    time.sleep(1.25) 
    midiout.send_message(note_off2)
    
# playnote(4)

def off_note(n):
    print("sending note_off for ")
    print(n.note)
    note_off = channel_message(NOTE_OFF, n.note + 24, 0, ch = n.channel)
    midiout.send_message(note_off)

def on_note(n,v, channel = 1):
    print("playing note ")
    print(n)
    note_on = channel_message(NOTE_ON, n + 24, v, ch = channel) #ch)
    # print("on_note")
    # print(note_on)
    # print("velocity")
    # print(v)
    midiout.send_message(note_on)



def getNote_from_0_to_7(num):
    elemstring ="b" + str(num.strip())
    elem = driver.find_element_by_id(elemstring)
    elem.click()
    out = driver.find_element_by_id("input")
    note = out.get_attribute('value')
    return note

def read_settings():
  global num_for_three_channels
  global num_for_two_channels
  global velocity
  global delay
  global duration
  global threshold0
  global threshold1
  global threshold2
  global threshold3
  global thresholds
  webPage = driver.find_element_by_id("durationId")
  duration = webPage.get_attribute('value')
  webPage = driver.find_element_by_id("num_for_three_channels")
  num_for_three_channels = webPage.get_attribute('value')
  webPage = driver.find_element_by_id("num_for_two_channels")
  num_for_two_channels = webPage.get_attribute('value')
  webPage = driver.find_element_by_id("velocityId")
  velocity = int(webPage.get_attribute('value'))
  webPage = driver.find_element_by_id("delayId")
  delay = webPage.get_attribute('value')
  webPage = driver.find_element_by_id("threshold0")
  threshold0 = webPage.get_attribute('value')
  webPage = driver.find_element_by_id("threshold1")
  threshold1 = webPage.get_attribute('value')
  webPage = driver.find_element_by_id("threshold2")
  threshold2 = webPage.get_attribute('value')
  webPage = driver.find_element_by_id("threshold3")
  threshold3 = webPage.get_attribute('value')
  thresholds=[int(threshold0),int(threshold1),int(threshold2),int(threshold3)]

  # print("updating settings")


def getNote_from_0_to_3(num):
    map = [1,3,5,7]
    elemstring ="b" + str(map[num])
    elem = driver.find_element_by_id(elemstring)
    elem.click()
    out = driver.find_element_by_id("input")
    note = out.get_attribute('value')
    return note


class Play:
  last_check_time = datetime.datetime.now()
  notes = deque()
  notes_off = deque()
  played_notes = deque()
  # s = 
  v = 11

  def __init__(self):
    devs = comports()
    for i in range(len(devs)-1):
      print(f'{i}":"{devs[i]}')
    com = int(input())
    print("connecting to port ") 
    # dev = devs[len(devs) - 1].device
    dev = devs[com].device
    print(dev)
    # found_device = "COM1"
    # for i in devs:
    #   if "USB" in i.device:
    #     found_device = i.device
    # print(found_device)
    self.s = Serial(dev, 9600, timeout=.1)
    self.last = [datetime.datetime.now()] * 5
    self.last[0] = datetime.datetime.now()
    self.last[1] = datetime.datetime.now()
    self.last[2] = datetime.datetime.now()
    self.last[3] = datetime.datetime.now()
    self.last[4] = datetime.datetime.now()

  def process_serial_data(self, data):
    currentDT = datetime.datetime.now()
    print("read")
    print(data)
    chime = data.split()[0]
    mvt = int(data.split()[1])
    if (mvt < thresholds[int(chime)]):
      return
    # print("mvt:")
    # print(mvt)
    # print("currentDT")
    # print(currentDT)
    # print(currentDT + datetime.timedelta(microseconds=int(delay)*1000))
    # print("lastofchime")
    # print(self.last[int(chime)])
    # print("chime:")
    # print(type(chime))
    # print(int(chime))
    if (currentDT > self.last[int(chime)] +  datetime.timedelta(microseconds=int(delay)*1000)):
      read = int(chime) #data #randint(0,3)
      pitch = getNote_from_0_to_3(read)
      self.add_note(pitch)
      self.last[int(chime)] = currentDT

  def does_Q_have_note(self, notes, check_note):
    for timed_note in notes:
      if (timed_note.note == check_note.note and timed_note.channel == check_note.channel):
      	return True
    return False

  def check_Q(self):
    print("len" + str(len(self.notes_off)))
    if len(self.notes_off) > 0:
      ntime = self.notes_off[0].time
      currentDT = datetime.datetime.now()
      if (currentDT > ntime):
        self.rm_note()

  def check_com(self):
    # s = serial.Serial('COM6')
    # print("reading com6")
    try:
      data = self.s.readline()[:-2] #the last bit gets rid of the new-line chars
     # data = re.findall(r'\d+', data)[0] 
    except  SerialException:
    	print("doh")

    if data:
      print("read:")
      data = data.decode("utf-8") 
      print(data)
      # print(type(data))
      # data = int.from_bytes(data, byteorder='big') - 48
      # print(type(data))
      # data = data[0] - 48
      # print("minus 48=")
      # print(data)
      self.process_serial_data(data)
      # print("playing ")
      # print(data)

  def update_settings(self):
    currentDT = datetime.datetime.now()
    if (currentDT  > self.last_check_time + datetime.timedelta(microseconds=freq_check_settings)):
      print(currentDT)
      self.last_check_time = datetime.datetime.now()
      read_settings()
      currentDT = datetime.datetime.now()
      print(currentDT)

  def runp(self):
    self.check_com()
    self.check_Q()
    self.update_settings()

  def rm_note(self):
    timed_note = self.notes_off.popleft()
    is_note_later_in_queue = self.does_Q_have_note(self.notes_off, timed_note)
    if not(is_note_later_in_queue):
      timed_note.time_off = datetime.datetime.now()
      self.played_notes.append(timed_note)
      off_note(timed_note)

  def add_note(self, pitch):
  	# notes()
    # print(type(pitch))
    global velocity
    # self.v = self.v + 1
    if (len(self.notes_off) > int(num_for_three_channels)):
      channel = random.randint(1,3)
    elif (len(self.notes_off) > int(num_for_two_channels)):
      channel = random.randint(1,2)
    else:
      channel = 1
    # print(pitch)
    # print(type(pitch))
    on_note(int(pitch), int(velocity),channel) # add delay for 1/4note...
    currentDT = datetime.datetime.now()
    d = (int(duration) * 1000)
    # print(d)
    note_off_time = currentDT + datetime.timedelta(microseconds=d)
    # print ("Current Microsecond is: %d" % currentDT.minute)
    tn= TimedNote(int(pitch),note_off_time,channel)
    self.notes_off.append(tn)




def connect_midi():
  global midiout
  midiout = rtmidi.MidiOut()
  available_ports = midiout.get_ports()

  # here we're printing the ports to check that we see the one that loopMidi created. 
  # In the list we should see a port called "loopMIDI port".
  print(available_ports)

  # Attempt to open the port
  if available_ports:
      midiout.open_port(1)
  else:
      midiout.open_virtual_port("My virtual output")





p = Play()
connect_midi()
driver = webdriver.Chrome()
curr_dir = os.getcwd()
driver.get("file:///" + curr_dir + "/wc.html")
# time.sleep(4)
# elem1 = driver.find_element_by_id("b1")
# elem2 = driver.find_element_by_id("b2")
# elem3 = driver.find_element_by_id("b3")
out = driver.find_element_by_id("input")

while True:
	p.runp();
# s = serial.Serial('COM6')
# while True:
# 	data = s.readline()[:-2] #the last bit gets rid of the new-line chars
# 	if data:
# 		print(data)
# 		res = s.read()
# print(res)
del midiout
driver.close()
# freakonomics  on the media