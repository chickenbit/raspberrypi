# Using a camera

## USB Camera setup

To verify plug and play...plug in the USB camera and use the *lsusb* command before playing

```
pi@raspberrypi:~/Documents/raspberrypi $ lsusb
Bus 001 Device 011: ID 0ac8:3420 Z-Star Microelectronics Corp. Venus USB2.0 Camera
Bus 001 Device 005: ID 0079:0006 DragonRise Inc. PC TWIN SHOCK Gamepad
Bus 001 Device 007: ID 05ac:921c Apple, Inc. A1082 [Cinema HD Display 23"]
Bus 001 Device 009: ID 05ac:0304 Apple, Inc. Mighty Mouse [Mitsumi, M1152]
Bus 001 Device 008: ID 05ac:0220 Apple, Inc. Aluminum Keyboard (ANSI)
Bus 001 Device 006: ID 05ac:1006 Apple, Inc. Hub in Aluminum Keyboard
Bus 001 Device 004: ID 05ac:911c Apple, Inc. Hub in A1082 [Cinema HD Display 23"]
Bus 001 Device 003: ID 0424:ec00 Standard Microsystems Corp. SMSC9512/9514 Fast Ethernet Adapter
Bus 001 Device 002: ID 0424:9514 Standard Microsystems Corp. SMC9514 Hub
Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
```

## Capturing Still Images

Start with the [Using a standard USB webcam](https://www.raspberrypi.org/documentation/usage/webcams/) post

## Monitoring video

Basics of using [motion](https://motion-project.github.io/) [ref](https://www.linux.com/learn/how-operate-linux-spycams-motion)

```
pi@raspberrypi:~ $ sudo motion
[0:motion] [NTC] [ALL] conf_load: Processing thread 0 - config file /etc/motion/motion.conf
[0:motion] [NTC] [ALL] motion_startup: Motion 4.0 Started
[0:motion] [NTC] [ALL] motion_startup: Logging to file (/var/log/motion/motion.log)
```

Then open your browser to [localhost:8081](http://localhost:8081/)
