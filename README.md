# Project 3: Log Analysis
### by Gokul S

Build an internal reporting tool project, part of the Udacity [Full Stack Web Developer Nanodegree](https://in.udacity.com/course/full-stack-web-developer-nanodegree--nd004).).

## Project contents

This project consists for the following files:

* output.png - output screenshot
* log.py - main Python script to run.
* newsdata.zip - database file (Udacity supplied)

## Functions in log.py

* connect(): Connects to the PostgreSQL database and returns a database 
  connection.
* article(): Prints most popular three articles of all time.
* authors(): Prints most popular article authors of all time.
* status(): Print days on which more than 1% of requests lead to errors.

## How to Run Project

* Install Python3, Vagrant and VirtualBox.

* Download this project

* Launch Vagrant VM by running vagrant up, you can the log in with vagrant ssh

* Unzip newsdata.zip

* Setup Database, Loading the data use the following command
    ```sh
    psql -d news -f newsdata.sql;
    ```

* To execute the program, run
    ```sh
    python log.py
    ```
