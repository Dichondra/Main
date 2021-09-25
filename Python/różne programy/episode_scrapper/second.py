#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 09:21:26 2021

@author: franek
"""


new_episodes = ["Season 5 Episode 1","Season 5 Episode 20","Season 5 Episode 21","Season 5 Episode 22","Season 5 Episode 23","Season 5 Episode 24"]
encode = "utf-8"


def mail_sender():
    print("hello")
    conn = smtplib.SMTP('smtp.gmail.com', 587)
    conn.ehlo()
    conn.starttls()
    conn.login('pythonorszulak@gmail.com', 'cjvtsybxdatgcdhc')
    conn.sendmail('pythonorszulak@gmail.com', "franekorszulak@gmail.com", 'Subject: Boku no hero academia episode!\n\nAttention!\n\nYour favourite show is available today!\n\n')
    #conn.sendmail('pythonorszulak@gmail.com', "asia.widla@gmail.com", 'Subject: Boku no hero academia episode!\n\nAttention!\n\nYour favourite show is available today!\n\n')

    conn.quit()
    
def checker_new_episodes(new_episodes,page_string):
    found = False
    for episode in new_episodes:
        if episode in page_string:
            found = True
            new_episodes.remove(episode)
    return found