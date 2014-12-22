Raspberry Pi monitoring systems
========================================

This is a set of ansible scripts that can be used to build a temperature and 
humidity logging station out of a raspberry pi.

=== Getting Started ===
-----------
You will need a raspberry pi model B, and an SD card loaded with a newer version of Raspbian. The 
following versions of raspbian have been tested and confirmed working:
* 2014-09-09-wheezy-raspbian
* 2014-06-20-wheezy-raspbian
* 2014-01-07-wheezy-raspbian

You can find instructions on installing Raspbian to an SD card here: 
http://www.raspberrypi.org/documentation/installation/installing-images/README.md

=== Building the Hardware ===
-----------
For environmental monitoring, this system requires you to build a simple circuit board and attach 
it to your raspberry pi. Full instructions for the circuit are here:
http://programmingace.com/2014/12/11/raspberry-pi-monitoring-platform-the-hardware/


=== Security Considerations ===
-----------
These scripts do not build a 'secure' image. The default root username and password are left as-is.
DO NOT leave this system connected to an untrusted network (such as the internet).
This script loads an SSH key for the ansible user. You can find the respective 
private SSH key in the "ssh_keys" directory of the repo.

=== Installing ===
-----------
We will be setting up the raspberry pi using Ansible. If you don't already have Ansible installed, 
it should be in the major repos already (mac homebrew, Fedora/EPEL, Ubuntu). Otherwise:
http://docs.ansible.com/intro_installation.html

** Finding your pi's IP address: **
You will need the IP address of your raspberry pi in order for Ansible to install the configuration.
The raspberry pi foundation gives several methods for finding your IP address here:
http://www.raspberrypi.org/documentation/troubleshooting/hardware/networking/ip-address.md

** From your PC: **
If you have strict hostkey checking turned on for SSH (which you probably do), 
you'll need to SSH into the raspberry pi once before running these scripts. 
This will add the pi's hostkey to your SSH configuration. The default login
is: 
username: pi 
password: raspberry

You will need to edit the 'inventory' file in the 'playbooks' folder of the repo.
Under [raspberry_pi] replace the IP address with the address to your Pi.

There are several different configurations you can choose from that perform 
different tasks.

- raspberry_pi.yml - Runs updates, sets up ssh keys, removes wolfram alpha packages, resizes SD card
- env_monitor_no_screen.yml - Same as raspberry_pi.yml, plus sets up a temperature and humidity 
                              monitoring system
- env_monitor_with_screen.yml - Same as above, but displays output on an adafruit LCD touchscreen

Configuring the Raspberry Pi:
To configure the pi, run the following command. Expect the build to take about half an hour:

ansible-playbook -i inventory <<select .yml file from the options above>> -u pi --ask-pass

When prompted for a password, use 'raspberry'

=== Viewing the Data ===
-----------
This monitoring system records and presents data using the open source tool Graphite. The graphite 
dashboard is already up and running, you'll just need to select how you want to display the data. 
You can find the dashboard at:
http://<IP of raspberry pi>>/dashboard/

The temperature and humidity readings are under the category 'environment'.

You can read more about graphite here:
https://graphite.readthedocs.org/en/latest/

