from selenium import webdriver
import HtmlTestRunner
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
class selenium_about(unittest.TestCase):
 def test_about(self):   
  driver = webdriver.Chrome(executable_path='.\drivers/chromedriver')
  driver.get('https://www.selenium.dev/')
  driver.maximize_window()
  time.sleep(1)


  WebDriverWait(driver,5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/header/nav/div/ul/li[2]/a')))\
    .click()
  time.sleep(5)
  WebDriverWait(driver,5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/header/nav/div/ul/li[2]/div/a[1]')))\
    .click()
  time.sleep(5)
########################################################    


  WebDriverWait(driver,5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/header/nav/div/ul/li[2]/a')))\
    .click()
  time.sleep(5)



  WebDriverWait(driver,5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/header/nav/div/ul/li[2]/div/a[2]')))\
    .click()
  time.sleep(5)
###########################################################

  WebDriverWait(driver,5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/header/nav/div/ul/li[2]/a')))\
    .click()
  time.sleep(5)

  WebDriverWait(driver,15)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/header/nav/div/ul/li[2]/div/a[7]')))\
    .click()
  time.sleep(5)
############################################################

  WebDriverWait(driver,5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/header/nav/div/ul/li[2]/a')))\
    .click()
  time.sleep(5)

  WebDriverWait(driver,5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/header/nav/div/ul/li[2]/div/a[4]')))\
    .click()
  time.sleep(5)
############################################################################################

  WebDriverWait(driver,5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/header/nav/div/ul/li[2]/a')))\
    .click()
  time.sleep(5)

  WebDriverWait(driver,5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/header/nav/div/ul/li[2]/div/a[5]')))\
    .click()
  time.sleep(5)
########################################################
  WebDriverWait(driver,5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/header/nav/div/ul/li[2]/a')))\
    .click()
  time.sleep(5)

  WebDriverWait(driver,5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/header/nav/div/ul/li[2]/div/a[6]')))\
    .click()
  time.sleep(5)
#################################################################

if __name__=='__main__':
 unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='resultados test abaut'))