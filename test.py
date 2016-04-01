# -*- coding: utf-8 -*-
from fixture import driver


def test_login(driver):
    driver.get("https://mail.rambler.ru/")
    driver.find_element_by_name("login").send_keys("autotestselenium")
    driver.find_element_by_name("password").send_keys("creative")
    driver.find_element_by_xpath("//button[@type=\"submit\"]").click()





