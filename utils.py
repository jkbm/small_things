#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import sys
import requests


def progress_bar(y=100):
    """
    Progress bar visualisation
    """

    step = y / 100
    out = ""
    for x in range(1, 101):
        out = "#" * (x // 5)
        out = "[" + out + "] Progress: " + str(round(
            ((step * x) / 100), 2)) + "%."
        sys.stdout.write('\r' + out)
        sys.stdout.flush()
        time.sleep(0.1)


def progress_bar_status(status=200,
                        summary=1000,
                        interupt=0.1,
                        started=None,
                        message="Progress:"):
    """
    Progress bar managable

    Params:
        status(int) - progress status(i.e. completed N)
        summary(int) - finish goal(M needed to complete)
        interupt(float) - time.sleep value to see the progress if it displays too fast
        started(time) - time.time value when the process started(used to predict ETA)
        message(str) - custom message to display
    """
    status = float(status)
    summary = float(summary)
    progress = status / (summary / 100)

    estimation = " "
    if started:
        elapsed = time.time() - float(started)
        pace = elapsed / status
        estimation = "ETA: {0} seconds".format(
            str(round((pace * (summary - status)), 2)))
    out = "#" * (int(progress // 5))
    out = "[{0}] {1} {2}%. {3}.".format(out, message, str(round(progress, 2)),
                                        estimation)
    sys.stdout.write('\r' + out)
    sys.stdout.flush()
    time.sleep(interupt)


def read_config(filepath):
    """Read config file from filepath

    Params:
        filepath(str) - path to config file
    Return:
        config(dict) - config dict
    """

    config = {}
    with open(filepath, "r") as f:
        config_s = f.read().split("\n")
    for l in config_s:
        if l != "" and "#" not in l:
            try:
                k, v = l.strip().replace(" ", "").split("=")
                config[k] = eval(v)
            except:
                print("Wrong line: " + l)

    return config