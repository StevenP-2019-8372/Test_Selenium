from selenium import webdriver
import HtmlTestRunner
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
class selenium_blog(unittest.TestCase):

 def test_blog(self):
  driver = webdriver.Chrome(executable_path='.\drivers/chromedriver')
  driver.get('https://www.selenium.dev/')
  driver.maximize_window()
  time.sleep(1)


  WebDriverWait(driver,5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/header/nav/div/ul/li[7]/a')))\
    .click()
  time.sleep(5)

  WebDriverWait(driver,5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/div/div[1]/div/aside[1]/div/nav/ul/li/ul/li[2]/a')))\
    .click()
  time.sleep(5)

  WebDriverWait(driver,5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/div/div[1]/div/aside[1]/div/nav/ul/li/ul/li[3]/a')))\
    .click()
  time.sleep(5)
  WebDriverWait(driver,5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/div/div[1]/div/aside[1]/div/nav/ul/li/ul/li[4]/a')))\
    .click()
  time.sleep(5)

  WebDriverWait(driver,5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/div/div[1]/div/aside[1]/div/nav/ul/li/ul/li[5]/a')))\
    .click()
  time.sleep(5)

  WebDriverWait(driver,5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/div/div[1]/div/aside[1]/div/nav/ul/li/ul/li[6]/a')))\
    .click()
  time.sleep(5)
  WebDriverWait(driver,5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/div/div[1]/div/aside[1]/div/nav/ul/li/ul/li[7]/a')))\
    .click()
  time.sleep(5)
  WebDriverWait(driver,5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/div/div[1]/div/aside[1]/div/nav/ul/li/ul/li[8]/a')))\
    .click()
  time.sleep(5)
  WebDriverWait(driver,5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/div/div[1]/div/aside[1]/div/nav/ul/li/ul/li[9]/a')))\
    .click()
  time.sleep(5)
  WebDriverWait(driver,5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/div/div[1]/div/aside[1]/div/nav/ul/li/ul/li[10]/a')))\
    .click()
  time.sleep(5)
  WebDriverWait(driver,5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/div/div[1]/div/aside[1]/div/nav/ul/li/ul/li[11]/a')))\
    .click()
  time.sleep(5)
  WebDriverWait(driver,5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/div/div[1]/div/aside[1]/div/nav/ul/li/ul/li[12]/a')))\
    .click()
  time.sleep(5)
  WebDriverWait(driver,5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/div/div[1]/div/aside[1]/div/nav/ul/li/ul/li[13]/a')))\
    .click()
  time.sleep(5)




if __name__=='__main__':
 unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='resultados test blog'))