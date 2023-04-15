from selenium import webdriver
import HtmlTestRunner
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

class selenium_download(unittest.TestCase):

 def test_download(self):
  driver = webdriver.Chrome(executable_path='.\drivers/chromedriver')
  driver.get('https://www.selenium.dev/')
  driver.maximize_window()
  time.sleep(1)


  WebDriverWait(driver,5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/header/nav/div/ul/li[3]/a')))\
    .click()
  time.sleep(5)
  WebDriverWait(driver,5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/div/main/div[2]/div[2]/div/div/p[1]/a')))\
    .click()
  time.sleep(5)
  WebDriverWait(driver,5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/div/main/div[2]/div[2]/div/div/p[1]/a')))\
    .click()
  time.sleep(5)
  

if __name__=='__main__':
 unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='resultados test download'))