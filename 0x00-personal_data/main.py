#!/usr/bin/env python3
"""
Main file
"""
filter_datum = __import__('filtered_logger').filter_datum


fields = ["password", "date_of_birth"]
messages = ["name=Nick;email=nicholasodhiambo2015@gmail.com;password=eggcellent;date_of_birth=12/12/1986", "name=Anna;email=muturianna@gmail.com;password=anime;date_of_birth=1993"]

for message in messages:
    print(filter_datum(fields, 'xxx', message, ';'))
