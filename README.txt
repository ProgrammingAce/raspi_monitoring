Raspberry Pi monitoring systems
========================================

This is a set of ansible scripts that can be used to build a temperature and 
humidity logging station out of a raspberry pi.

If you have strict hostkey checking turned on for SSH (which you probably do), 
you'll need to SSH into the raspberry pi once before running these scripts. 
This will add the pi's hostkey to your SSH configuration. The default login
is 
username: pi 
password: raspberry

There are several different configurations you can choose from that perform 
different tasks.

- raspberry_pi.yml - Runs updates, sets up ssh keys, removes wolfram alpha packages, resizes SD card
- env_monitor_no_screen.yml - Same as raspberry_pi.yml, plus sets up a temperature and humidity 
                              monitoring system
- env_monitor_with_screen.yml - Same as above, but displays output on an adafruit LCD touchscreen

To configure the pi, run the following command:

ansible-playbook -i inventory <<select .yml file from the options above>> -u pi --ask-pass

When prompted for a password, use 'raspberry'

This script loads an SSH key for the ansible user. You can find the respective 
private SSH key in the ssh_keys directory.


