# -*- coding: utf-8 -*-
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys


class Application(object):
    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url
        self.wait = WebDriverWait(driver, 60)

    def go_to_home(self):
        self.driver.get(self.base_url)

    def logout(self):
        driver= self.driver
        driver.find_element_by_xpath("//span[contains(@class,'b-rambler-topline-user__name')]").click()
        driver.find_element_by_xpath("//a[text()='Выйти']").click()

    def login(self, user):
        driver = self.driver
        driver.find_element_by_name("login").send_keys(user.username)
        driver.find_element_by_name("password").send_keys(user.password)
        driver.find_element_by_xpath("//select[@name='domain']/option[@value='@rambler.ru']").click()
        driver.find_element_by_xpath("//button[@type=\"submit\"]").click()

    def is_logged(self):
        driver = self.driver
        try:
            self.wait.until(presence_of_element_located((By.XPATH, "//span[contains(@class,'asideName mailboxName')]")))
            return True
        except WebDriverException:
            return False

    def is_logout(self):
        driver = self.driver
        try:
            self.wait.until(presence_of_element_located((By.XPATH, "//button[@type=\"submit\"]")))
            return True
        except WebDriverException:
            return False

    def verify_Mail(self):
        driver = self.driver
        writeMail = "//button[@title=\"Написать письмо\"]"
        komy = "//input[contains(@class,'uiAutocompleteTextInput')]"
        subject = "subject"
        attach = "file"
        send = "//button[@title=\"Отправить письмо\"]"
        delmail = "//button[@title=\"Удалить письмо\"]"

        if len(driver.find_elements_by_xpath(writeMail)) > 0:
            driver.find_element_by_xpath(writeMail).click()
            print "Кнопка Написать присутствует и прожата"

        driver.find_element_by_xpath(komy).click
        if len(driver.find_elements_by_xpath(komy)) > 0:
            print "Кому присутствует"

        if len(driver.find_elements_by_id(subject)) > 0:
            print "Тема присутствует"

        if len(driver.find_elements_by_xpath(send)) > 0:
            print "Кнопка отправить присутствует"

        if len(driver.find_elements_by_xpath(delmail)) > 0:
            print "Кнопка удалить присутствует"



