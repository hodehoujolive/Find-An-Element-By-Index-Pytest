import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestIndex():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_index(self):
    self.driver.get("https://www.lambdatest.com/selenium-playground/input-form-demo")
    #self.driver.set_window_size(1200, 763)
    self.driver.find_element(By.NAME, "country").click()
    country = 104
    dropdown = self.driver.find_element(By.NAME, "country")
    option = dropdown.find_element(By.XPATH, "//*[@id='seleniumform']//select/option[{}]".format(country))
    option.click()

    with open('country.txt', 'a') as f:
       f.write(" Selected country is : "+ option.text)
       f.write('\n')

    #self.driver.execute_script("window.scrollTo(0,198)")
    time.sleep(10)