#!/usr/bin/python

import re
import os
import sys
import time
import platform
import subprocess
import netifaces
from socket import *

CARBON_SERVER = '127.0.0.1'
CARBON_PORT = 2003

delay = 60
if len(sys.argv) > 1:
  CARBON_SERVER = int( sys.argv[1] )
  CARBON_PORT = int( sys.argv[2] )

def get_environment():
  # Returns Temperature as first value and humidity as the second
  output = subprocess.check_output(["/usr/local/bin/Adafruit_DHT", "2302", "4"]);
  matches = re.search("Temp =\s+([0-9.]+)", output)
  if (not matches):
    return (0, 0)

  temp = float(matches.group(1))

  # Convert C to F
  temp = 9.0/5.0 * temp + 32
  # search for humidity printout
  matches = re.search("Hum =\s+([0-9.]+)", output)

  if (not matches):
    return (0, 0)
  humidity = float(matches.group(1))

  return (temp, humidity)

while True:

  # Clear the screen
  print "\033[2J\033[1;1H"

  sock = socket()
  try:
    sock.connect( (CARBON_SERVER,CARBON_PORT) )
  except:
    print "Couldn't connect to %(server)s on port %(port)d. Retrying in 5 minutes" % { 'server':CARBON_SERVER, 'port':CARBON_PORT }
    time.sleep(300)
    print "Trying to reconnect to server."
    continue

  now = int( time.time() )
  lines = []
  environment = get_environment()

  # If we received double zeroes from the sensor, skip the value
  if (environment[0] == 0 and environment[1] == 0):
    print "Received bad values from sensor, retrying in 10 seconds\n"
    time.sleep(10)
    continue

  lines.append("environment.temperature %s %d" % (environment[0],now))
  lines.append("environment.humidity %s %d" % (environment[1],now))
  message = '\n'.join(lines) + '\n' # Each line must end with a newline

  # Set the screen to white on black
  print "\033[0m\033[J"

  # Print information to the screen, set the newlines using ANSI codes
  print "\033[1;1HTemperature: %s\n" % environment[0]
  print "\033[2;1HHumidity:    %s\n" % environment[1]

  i = 3

  for interface in netifaces.interfaces():
    for link in netifaces.ifaddresses(interface)[netifaces.AF_INET]:
      print "\033[%d;1HIP:          %s\n" % (i, link['addr'])
      i += 1

  sock.sendall(message)
  sock.close()
  time.sleep(delay)
