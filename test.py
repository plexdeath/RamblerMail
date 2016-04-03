# -*- coding: utf-8 -*-
from fixture import ramblerapp
from RamblerModels.user import User
from selenium import webdriver
from RamblerModels.application import Application

def test_login(ramblerapp):
    ramblerapp.go_to_home()
    ramblerapp.login(User.Admin())
    assert ramblerapp.is_logged
    ramblerapp.logout()
    assert ramblerapp.is_logout
