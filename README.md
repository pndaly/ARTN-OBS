Arizona Robotic Telescope Network Observation Block Scheduler
-------------------------------------------------------------

Welcome to the **A**rizona **R**obotic **T**elescope **N**etwork **O**bservation **B**lock 
**S**cheduler (*ARTN-OBS*) which generates an observing schedule for any given night for
any (valid) telescope and instrument combination within the network.

## Quick Start

```bash
  % source etc/OBS.sh `pwd`

  % python3.7 artn_schedule.py --help
    usage: artn_schedule.py [-h] [--instrument INSTRUMENT] [--telescope TELESCOPE]
                            [--verbose]

    ARTN Telescope Scheduler

    optional arguments:
      -h, --help            show this help message and exit
      --instrument INSTRUMENT
                            Instrument, defaults to 'Mont4k', choices: ['90Prime', 'BCSpec', 'Mont4k', 'BinoSpec', 'Vatt4k']
      --telescope TELESCOPE
                            Telescope, defaults to 'Kuiper', choices: ['Bok', 'Kuiper', 'MMT', 'Vatt']
      --verbose             if present, produce verbose output
```

## Pre-Requisites

* Linux (we use Ubuntu 18.04 LTS)
* Python 3.7 (it will not work with Python < 3.6)
* PostGreSQL 12.x (but will probably work with earlier versions)

## Get The Software

* Obtain a copy of the software from [GitHub](https://github.com/pndaly/ARTN-OBS).

* Install dependencies:

    ```bash
    % pip3 install --upgrade pip
    % pip3 install -r requirements.txt
    ```

## Create (Get) The Dockerized Database 

We dockerize the database, so a utility is also provided for that:
    
    ```bash
      % bash ${OBS_DOCKER}/docker.sh --help
    ```

This script is based upon `${OBS_DOCKER}/docker.template.sh` which contains dummy credentials. 
Edit as you see fit but (as a minimum) you should change:

```bash
my_image="artn/postgres-12:q3c2"
my_password="db_secret"
my_username="artn"
my_volume=${HOME}
```

If you decide to use Docker, remember to restart the container after a reboot via root's `crontab` (and, of 
course, replace `<path_to_shell_script>` with your installation path in the following):
    
    ```
      @reboot bash <path_to_shell_script>/docker.sh --command=start --name=artn
    ```

NB: We utilize the Q3C spatial indexing extensions. The file `${OBS_DOCKER}/Dockerfile.artn` shows 
how to build a new image with these extensions. If such a new image is created, the 
`${OBS_DOCKER}/docker.sh` script would have to be edited to reflect the new image. We can provide
a tarball of our dockerized container upon request.

## Configure For Local Site

You should now *copy* `${OBS_ETC}/OBS.template.sh` and edit the copy to suit your site.

```bash
% cp ${OBS_ETC}/OBS.template.sh ${OBS_ETC}/OBS.sh
% vi ${OBS_ETC}/OBS.sh
```

## Test(s)

```bash
  % cd ${OBS_TESTS}
  % python3.7 -m pytest artn_test.py
```

## IERS Updates

Sometime during 2019 astropy/astroplan broke due to the IERS ephemeris server at USNO going offline. To fix this,
the startup script will load the new ephemeris *every* time it is run. Feel free to comment out this line.

------------------------------------------------------------

Last Updated: 2020619
