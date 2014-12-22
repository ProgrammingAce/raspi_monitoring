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
Instructions for building the required hardware are here:  
https://github.com/ProgrammingAce/raspi_monitoring/wiki/Hardware


=== Security Considerations ===
-----------
These scripts do not build a 'secure' image. The default root username and password are left as-is.
DO NOT leave this system connected to an untrusted network (such as the internet).
This script loads an SSH key for the ansible user. You can find the respective 
private SSH key in the "ssh_keys" directory of the repo.

=== Installing ===
-----------
Instructions for setting up your monitoring system are here:  
https://github.com/ProgrammingAce/raspi_monitoring/wiki/Installation

=== Viewing the Data ===
-----------
This monitoring system records and presents data using the open source tool Graphite. The graphite 
dashboard is already up and running, you'll just need to select how you want to display the data. 
You can find the dashboard at:  
http://{IP of raspberry pi}/dashboard/

The temperature and humidity readings are under the category 'environment'.

You can read more about graphite here:
https://graphite.readthedocs.org/en/latest/

