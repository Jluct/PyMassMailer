# !/usr/bin/env python3
# coding:utf-8

import smtplib
from ConfigData import ConfigData
from SenderMail import SenderMail
from Helper.DataParser import DataParser

if __name__ == "__main__":
    conf = ConfigData()

    data_parser = DataParser(conf.get_section('data'))
    address = data_parser.getData()
    sender = SenderMail(conf, smtplib)
    sender.set_address(address).send_all()
