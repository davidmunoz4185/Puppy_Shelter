# SWISS TOURNAMENT

This Repository simulates how a Swiss Classification works

### First Steps

You are required to have the following Software:

* Virtual Box
* Vagrant

#### Virtual Box

VirtualBox is a general-purpose full virtualizer for x86 hardware, targeted at server, desktop and embedded use. You can download it in:

https://www.virtualbox.org/wiki/Downloads

#### Vagrant

In addition, you will need vagrant in order to create and configure lightweight, reproducible, and portable development environments:

https://www.vagrantup.com/downloads.html

#### Clone it!!!

`git clone https://github.com/davidmunoz4185/Swiss-Tournament.git`

#### Setup it!!!

	$ vagrant up
	$ vagrant ssh

#### Runt it!!!

It is almost done, just 2 steps:

* Init DataBase
* Run test

##### Init DataBase

	$ cd /vagrant/tournamet
	$ psql
	psql (9.3.15)
	Type "help" for help.

	vagrant=> \i tournament.sql
	DROP DATABASE
	CREATE DATABASE
	You are now connected to database "tournament" as user "vagrant".
	CREATE TABLE
	CREATE TABLE
	CREATE VIEW
	tournament=>
	tournament=>
	tournament=> \q

##### Run Test

	$ python tournament_test.py`


