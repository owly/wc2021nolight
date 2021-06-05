# https://us02web.zoom.us/j/85289368735
 # .\mos158\mosquitto_sub.exe -h localhost -v -t test_channel
# https://tutorials-raspberrypi.com/raspberry-pi-mqtt-broker-client-wireless-communication/
 # cd .\Dropbox\arduino\; python .\play_from_serial.py
import serial
from serial import Serial
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys
import datetime		
import time
#from music import *        # import music library
#import rtmidi
import re 
from time import sleep
import random
import glob
import os
#import pandas as pd
import sys
import asyncio
import requests 
from serial.tools.list_ports import comports
#from rtmidi.midiconstants import (ALL_NOTES_OFF, ALL_SOUND_OFF, BALANCE, BANK_SELECT_LSB,
#                                  BANK_SELECT_MSB, BREATH_CONTROLLER, CHANNEL_PRESSURE,
 #                                 CHANNEL_VOLUME, CONTROL_CHANGE, DATA_ENTRY_LSB, DATA_ENTRY_MSB,
  #                                END_OF_EXCLUSIVE, EXPRESSION_CONTROLLER, FOOT_CONTROLLER,
   #                               LOCAL_CONTROL, MIDI_TIME_CODE, NOTE_OFF, NOTE_ON,
    #                              NRPN_LSB, NRPN_MSB, PAN, PITCH_BEND, POLY_PRESSURE,
     ##                            SONG_POSITION_POINTER, SONG_SELECT, TIMING_CLOCK)
from collections import deque
from serial.tools.list_ports import comports
#from apscheduler.schedulers.background import BackgroundScheduler
# importing the requests library 
# import requests 
# import paho.mqtt.client as mqtt
# from concurrent.futures import ThreadPoolExecutor
#from futures3.thread import ThreadPoolExecutor
#from futures3.process import ProcessPoolExecutor 
# MQTT_SERVER = "192.168.18.103"
MQTT_SERVER = "localhost"
MQTT_PATH = "test_channel"
 
#note = Note(C4, HN)        # create a middle C half note
#Play.midi(note)            # and play it!

print("1. Serial\n2. mqtt\n3. recordings")
mode = 1 #int(input())
if (mode == 1):
  devs = comports()
  for i in range(len(devs)):
    print(f'{i}":"{devs[i]}')
  com = 0 #int(input())
  print("connecting to port ") 
  # dev = devs[len(devs) - 1].device
  dev = devs[com].device
  print(dev)
  serial_com = serial.Serial(dev)
  print(serial_com)

if (mode == 3):
  offset = 0
  if (len(sys.argv) > 1):
    input_file = sys.argv[1]
  if (len(sys.argv) > 2):
    offset = sys.argv[2]
  else:
    list_of_files = glob.glob('./recordings/*') # * means all if need specific format then *.csv
    input_file = max(list_of_files, key=os.path.getctime) 
  offset = 0 #pd.to_timedelta(offset)
  # f = open(latest_file, "r")
  with open(input_file) as file:
    lines = [i.strip() for i in file]
  # TODO  add 5 lines like last one with 2 secs extra each
    # last_line = lines[len(lines) - 1]
    # last_line_time = last_line.split(" ")[0]
    # td = pd.to_timedelta(last_line_time)
    # tdd = td.timedelta(microseconds=int(delay)*1000)
    # data = last_line.split(" ")[1] +  " " + last_line.split(" ")[2] 
    # added_last_line = str(tdd) + " " + data
    # lines[len(lines)] = added_last_line
  # TODO  add 5 lines like last one with 2 secs extra each


def getCurrentFileIndex(lines):
  index = 0
  start_time = datetime.datetime.now()
  for l in lines: 
    now = datetime.datetime.now() + offset
    time = l.split(" ")[0]
    data = l.split(" ")[1] +  " " + l.split(" ")[2] 
    td = pd.to_timedelta(time)
    if (td < offset):
      index += 1
      continue
    if (td + start_time > now):
      return index





# defining the api-endpoint 
# API_ENDPOINT = "http://localhost:9876/drumify"
API_ENDPOINT = "http://drumbot.glitch.me/drumify"
#executor = ThreadPoolExecutor(2)


async def drumifyNotes(notes):
  print("drumify********")
  drumNotes = []
  for timed_note in notes:
    drumNote = {"pitch":timed_note.note,"velocity":40,"program":26,"startTime":timed_note.time,"endTime":timed_note.time_end}
    drumNotes.append(drumNote)
  data = {"notes": drumNotes
    ,"tempos":[{"qpm":120}]
    ,"totalTime":4
    ,"temperature":1}

  currentDT = datetime.datetime.now()
  print(currentDT)
  print("data=")
  print(data)

  # response = await loop.run_in_executor(executor, requests.get, url)
  #   return response.text
  # r = requests.post(url = API_ENDPOINT, data = data) 
  r = await loop.run_in_executor(executor, requests.post, url = API_ENDPOINT, data = data) 
  # extracting response text 
  re = r.text 
  print("response:%s"%re) 
# APPEND TO queue
  # to_json= json.dumps(data)



  # [{"pitch":48,"velocity":40,"program":26,"startTime":1.3293333333333308,"endTime":1.5793333333333308}
  # ,{"pitch":53,"velocity":40,"program":26,"startTime":1.838666666666665,"endTime":2.088666666666665}
  # ,{"pitch":57,"velocity":40,"program":26,"startTime":2.34,"endTime":2.59}
  # ,{"pitch":59,"velocity":40,"program":26,"startTime":2.9079999999999977,"endTime":3.1579999999999977}
  # ]
  # ,"tempos":[{"qpm":120}]
  # ,"totalTime":4
  # ,"temperature":1}


global midiout
threshold0 = 7
threshold1 = 7
threshold2 = 7
threshold3 = 7
thresholds=[threshold0,threshold1,threshold2,threshold3]
num_for_three_channels = 5
num_for_two_channels = 3
velocity = 50
velocityCode = """    if (mvt < 10):
      vel = 5
    elif (mvt < 50):
      vel = 75
    else:
      vel = 100
    return vel
"""
delay = 500
duration = 1500
freq_check_settings = 15522250

class TimedNote:
  def __str__(self):
    return f'note: {self.note}\ntime_end: {self.time_end}\ntime: {self.time}'

  def __init__(self, note, time = 0, channel=None, time_end = 0,):
    self.time = time
    # self.time_on 
    self.note = note	
    self.time_end = time_end
    self.channel = channel
  time = 0
  time_end = 0
  note = 0
  channel = 0
  # time_off = 0




def channel_message(command, *data, ch=None):
  # """Send a MIDI channel mode message."""
  command = (command & 0xf0) | ((ch if ch else 1) - 1 & 0xf)
  msg = [command] + [value & 0x7f for value in data]
  return msg

def off_note(n):
    now = datetime.datetime.now()
    print(str(now) + "sending note_off for " + str(n.note) + " in channel " + str(n.channel))
    note_off = channel_message(NOTE_OFF, n.note + 24, 0, ch = n.channel)
    #midiout.send_message(note_off)

def on_note(n,v, channel = 1):
    print(str(datetime.datetime.now()) + "playing note " + str(n))
    note_on = channel_message(NOTE_ON, n + 24, v, ch = channel) #ch)
    # print("VELOCITY: " + str(v))
    # print("on_note")
    # print(note_on)
    # print("velocity")
    # print(v)
#    midiout.send_message(note_on)



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
  global velocityCode
  global delay
  global duration
  global threshold0
  global threshold1
  global threshold2
  global threshold3
  global thresholds
  # freq_check_settings = 1522250
  webPage = driver.find_element_by_id("durationId")
  duration = webPage.get_attribute('value')
  webPage = driver.find_element_by_id("num_for_three_channels")
  num_for_three_channels = webPage.get_attribute('value')
  webPage = driver.find_element_by_id("num_for_two_channels")
  num_for_two_channels = webPage.get_attribute('value')
  webPage = driver.find_element_by_id("velocityId")
  velocityCode = webPage.get_attribute('value')
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

def getNote_from_0_to_1(num):
    # map = [1,3,5,7]
    first = datetime.datetime.now()

    elemNum = num * 4 + randint(0,3)
    elemstring ="b" +  elemNum
    # elemstring ="b" + str(map[num])

    a = datetime.datetime.now()
    # print("a" + str(a))
    elem = driver.find_element_by_id(elemstring)
    b = datetime.datetime.now()
    # print("b" + str(b))
    elem.click()
    c = datetime.datetime.now()
    # print("c" + str(c))
    out = driver.find_element_by_id("input")
    d = datetime.datetime.now()
    # print("d" + str(d))
    note = out.get_attribute('value')
    e = datetime.datetime.now()
    # print("e" + str(e))
    return note


def getNote_from_0_to_3(num):
    map = [1,3,5,7]
    first = datetime.datetime.now()

    elemstring ="b" + str(map[num])

    a = datetime.datetime.now()
    # print("a" + str(a))
    elem = driver.find_element_by_id(elemstring)
    b = datetime.datetime.now()
    # print("b" + str(b))
    elem.click()
    c = datetime.datetime.now()
    # print("c" + str(c))
    out = driver.find_element_by_id("input")
    d = datetime.datetime.now()
    # print("d" + str(d))
    note = out.get_attribute('value')
    e = datetime.datetime.now()
    # print("e" + str(e))
    return note


class Play:
  last_check_time = datetime.datetime.now()
  notes = deque()
  notes_off = deque()
  played_notes = deque()
  last_drum_run = datetime.datetime.now() 
  # s = 
  v = 11

  def __init__(self):
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
    print("chime:" + str(chime))
    mvt = int(data.split()[1])
    print("mvt:" + str(mvt))
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
      print("got pitch from chime:" + str(pitch))
      if (not pitch):
        return
      self.add_note(pitch,mvt)
      self.last[int(chime)] = currentDT
      addedTime = datetime.datetime.now()
      diff = addedTime - currentDT 
      # print("played in" + str(diff))

  def does_Q_have_note(self, notes, check_note):
    for timed_note in notes:
      if (timed_note.note == check_note.note and timed_note.channel == check_note.channel):
      	return True
    return False

  def check_Q(self):
    # print("len notes_off" + str(len(self.notes_off)) + "--")
    currentDT1 = datetime.datetime.now()
    # print("--------checkq currentDT:" + str(currentDT1))
    if len(self.notes_off) > 0:
      ntime = self.notes_off[0].time_end
      currentDT = datetime.datetime.now()
      if (currentDT > ntime):
        # print("currentDT:" + str(currentDT))
        # print("ntime:" + str(ntime))
        self.rm_note()
    # currentDT = datetime.datetime.now()

  def receive_data(self, data):
    # data = data.decode("utf-8") 
    starttime = datetime.datetime.now()
    print("receiveDATA() " + str(starttime))
    print(data)
    self.process_serial_data(data)
    # print("***process_serial_data:" + str(datetime.timedelta(datetime.datetime.now() - starttime)))
    print("end receiveDATA() " + str(datetime.datetime.now()))
    # self.runp()  #HACK!


  # def on_message(self, data):
  def on_message(self, client, userdata, msg):
    data = msg.payload
    self.receive_data(data)

    # print("read:")
    # data = data.decode("utf-8") 
    # print(data)
    # self.process_serial_data(data)
    # self.runp()  #HACK!

  def update_settings(self):
    currentDT = datetime.datetime.now()
    a = self.last_check_time + datetime.timedelta(microseconds=freq_check_settings)
    if (currentDT  > self.last_check_time + datetime.timedelta(microseconds=freq_check_settings)):
      print("update SETTINGS -----------")
      self.last_check_time = datetime.datetime.now()
      read_settings()
      currentDT = datetime.datetime.now()
      # print(currentDT)

  def check_drumify(self):
    currentDT = datetime.datetime.now()
    if ((currentDT - self.last_drum_run).seconds > 4):
      print("drumifying -----------")

      # if (currentDT.second % 5 == 0):
      print("mod 5 seconds")
      self.last_drum_run = currentDT
      self.drumify()

  def drumify(self):
    currentDT = datetime.datetime.now()
    # create array of notes last 5 sec
    notesToDrumify = []
    print("length %%%%")
    print(len(self.played_notes))
    for note in reversed(self.played_notes):
      # print("timeoff")
      # print(note.time_end)
      # print("15 secs ago")
      # print(currentDT - datetime.timedelta(seconds=5))
      if (note.time_end > (currentDT - datetime.timedelta(seconds=5))):
        notesToDrumify.append(note)
      # else:
      #   break
    print("drumify length %%%%")
    print(len(notesToDrumify))
    drumifyNotes(notesToDrumify)

  def runp(self):
    # self.check_com()
    self.check_Q()
    self.update_settings()
    # self.check_drumify()

  def rm_note(self):
    now = datetime.datetime.now()
    timed_note = self.notes_off.popleft()
    print("popping from notes_off " + str(timed_note.note) + str(now))
    is_note_later_in_queue = self.does_Q_have_note(self.notes_off, timed_note)
    if not(is_note_later_in_queue):
      timed_note.time_end = now
      self.played_notes.append(timed_note)
      # print("***--adding note to played--**")
      # print(timed_note)
##      off_note(timed_note) 
      # print("length ####")
      # print(len(self.played_notes))

  def getVelocityFromMVT(self, mvt):
    # exec(velocityCode)
    # return vel
    if (mvt > 127):
          vel = 127
    else:
      vel = mvt
    return vel

  def add_note(self, pitch, mvt):
    print("adding note " + str(pitch))
  	# notes()
    # print(type(pitch))
    vel = self.getVelocityFromMVT(mvt)
    # self.v = self.v + 1
    if (len(self.notes_off) > int(num_for_three_channels)):
      channel = random.randint(1,3)
    elif (len(self.notes_off) > int(num_for_two_channels)):
      channel = random.randint(1,2)
    else:
      channel = 1
    # print(pitch)
    # print(type(pitch))
   # on_note(int(pitch), int(vel),channel) # add delay for 1/4note...
    currentDT = datetime.datetime.now()

    d = self.getNoteDuration(vel)
    # print(d)
    note_off_time = currentDT + datetime.timedelta(microseconds=d)
    # print ("Current Microsecond is: %d" % currentDT.minute)
    # print("currtime:" + str(currentDT))
    # print("adding to notes_off")
    tn= TimedNote(int(pitch),currentDT, channel, note_off_time)
    # print(tn)
    self.notes_off.append(tn)
    # print("len" + str(len(self.notes_off)))
    # print(self.notes_off)


  def getNoteDuration(self, veloc):
    # based on global duration from settings
    d = (int(duration) * 1000)
    if (veloc > 75):
      d = d * 1.5
    if (veloc < 33):
      d = d / 2
    return d


def connect_midi():
  global midiout
#  midiout = rtmidi.MidiOut()
  available_ports = midiout.get_ports()

  # here we're printing the ports to check that we see the one that loopMidi created. 
  # In the list we should see a port called "loopMIDI port".
  print(available_ports)

  # Attempt to open the port
#  if available_ports:
#      midiout.open_port(1)
 # else:
#      midiout.open_virtual_port("My virtual output")


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
 
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(MQTT_PATH)
 
# The callback for when a PUBLISH message is received from the server.
# def on_message(client, userdata, msg):
#     print(msg.topic+" "+str(msg.payload))
    # more callbacks, etc
 



p = Play()
#connect_midi()
driver = webdriver.Chrome()
curr_dir = os.getcwd()
driver.get("http://localhost/~pi/wctone.html")
# time.sleep(4)
# elem1 = driver.find_element_by_id("b1")
# elem2 = driver.find_element_by_id("b2")
# elem3 = driver.find_element_by_id("b3")
out = driver.find_element_by_id("input")
sleep(5)

if (mode == 1):
  start_time = datetime.datetime.now()
  file_time = start_time.strftime("%y_%m_%d_%H_%M_%S")
  # file_time = datetime.datetime.timestamp()
  f = open("/home/pi/public_html/recordings/" + str(file_time) + ".txt", "w")

if (mode == 2):
  client = mqtt.Client()
  client.on_connect = on_connect
  client.on_message = p.on_message
   
  client.connect(MQTT_SERVER, 1883, 60)

  # def drum():
  #   p.drumify()
  # scheduler = BackgroundScheduler()
  # # scheduler = apscheduler.schedulers.blocking.BackgroundScheduler('apscheduler.job_defaults.max_instances': '3')
  # scheduler.add_job(drum, 'interval', seconds=15)
  # scheduler.start()
   
  # Blocking call that processes network traffic, dispatches callbacks and
  # handles reconnecting.
  # Other loop*() functions are available that give a threaded interface and a
  # manual interface.
  client.loop_start()

# client.loop_forever()

def check_serial():
  if (serial_com.in_waiting > 0):
    print("serial WAITING" + str(serial_com.in_waiting) + "  " +  str(datetime.datetime.now()))
    data = serial_com.readline()[:-2] #the last bit gets rid of the new-line chars
    print(data)
    if data:
      chime = data.split()[0]
      mvt = int(data.split()[1])
      data_to_send = str(int(chime)) + " " + str(mvt)
      p.receive_data(data_to_send)

if (mode == 3):
  recording_file_index = getCurrentFileIndex(lines)
  start_time = datetime.datetime.now()
  print("file index:"  + str(recording_file_index))


def check_recording_file():
  global recording_file_index
  global start_time
  l = lines[recording_file_index]
  now = datetime.datetime.now() + offset
  time = l.split(" ")[0]
  data = l.split(" ")[1] +  " " + l.split(" ")[2] 
  td = 0 #pd.to_timedelta(time)
  if (td + start_time < now):
    p.receive_data(data)
    recording_file_index = recording_file_index + 1
    if (recording_file_index >= len(lines)):
      start_time = datetime.datetime.now()
      recording_file_index = 0



while True:
  p.runp()
  if (mode == 1):
    check_serial()
  if (mode == 3):
    check_recording_file()

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





sched.shutdown()
