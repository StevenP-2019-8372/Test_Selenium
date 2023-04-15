from selenium import webdriver
import HtmlTestRunner
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

class selenium_buscar(unittest.TestCase):

 def test_buscar(self):
  driver = webdriver.Chrome(executable_path='.\drivers/chromedriver')
  driver.get('https://www.selenium.dev/')
  driver.maximize_window()
  time.sleep(1)


  WebDriverWait(driver,5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      'button.DocSearch.DocSearch-Button')))\
    .click()
  time.sleep(5)
  WebDriverWait(driver,5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input#docsearch-input.DocSearch-Input')))\
    .send_keys('chrome')
  time.sleep(5)
  WebDriverWait(driver,5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      'svg.DocSearch-Hit-Select-Icon')))\
    .click()


  time.sleep(5)

if __name__=='__main__':
 unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='resultados test buscar'))