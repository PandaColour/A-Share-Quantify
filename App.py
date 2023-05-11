#!/usr/bin/python3
# -*- coding: utf-8 -*-
import logging
import os


class App:
    def __init__(self):
        self.app_name = "A Share Quantify"

    def run(self):
        self._init_logger_()

    def _init_logger_(self):
        log_format = "%(asctime)s %(levelno)s : %(message)s"
        log_path = os.path.realpath("./log")
        if not os.path.exists(log_path):
            os.mkdir(log_path)
        log_file = os.path.join(log_path, "log.log")
        logging.basicConfig(filename=log_file,
                            level=logging.INFO,
                            format=log_format)
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        ch.setFormatter(logging.Formatter(log_format))
        logging.getLogger().addHandler(ch)
        logging.info("start " + self.app_name)
