#!/bin/bash

case "$1" in
	start)
		if [ -e "wemomonitor.pid" ] ; then # Checks if the file wemomonitor.pid exists
			echo wemo monitor is already running
		else
			echo starting wemo monitor
			nohup python WemoControl/wemo_insight.py $(cat /home/feature/myWemo.txt) > energy.log  2>&1&
			echo $! > wemomonitor.pid
		fi
		;;
	stop)
		if [ -e "wemomonitor.pid" ] ; then # Checks if the file wemomonitor.pid exists
			echo stopping wemo monitor
			kill -9 "$(cat wemomonitor.pid)" # Kills the job with PID stored in wemomonitor.pid
			rm wemomonitor.pid # Deletes the file wemomonitor.pid
		else
			echo wemo monitor is already stopped
		fi
		;;
	status)
		if [ -e "wemomonitor.pid" ] ; then # Checks if the file wemomonitor.pid exists
			echo wemo monitor is running
		else
			echo wemo monitor is not running
		fi
		;;
	*)
	  echo "Usage: wemo_monitor.sh {start | stop | status}" >&2
	  exit 3
	  ;;
esac
exit 0
