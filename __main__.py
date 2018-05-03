#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import path
import smtplib
from jinja2 import Template
from PyMassMailer.ConfigData import ConfigData
from PyMassMailer.SenderMail import SenderMail
from PyMassMailer.DataParser import DataParser
from PyMassMailer.TemplateEngine import TemplateEngine

if __name__ == "__main__":
    conf = ConfigData()
    data_parser = DataParser(conf.get_section('data'))
    address = data_parser.getData()
    engine = TemplateEngine(Template)
    sender = SenderMail(conf, smtplib, engine)
    sender.set_address(address).send_all(
        open(
            path.normpath('templates/test.html'),
            'r',
            encoding='utf-8'
        ).read().encode('ascii', 'ignore')
    )
