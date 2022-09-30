import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures('driver')
class TestIndex():
  
  def test_index(self, driver):
    driver.get("https://www.lambdatest.com/selenium-playground/input-form-demo")
    driver.find_element(By.NAME, "country").click()

    country_index = 104
    dropdown = driver.find_element(By.NAME, "country")
    option = dropdown.find_element(By.XPATH, "//select[@name='country']/option[{}]".format(country_index))
    option.click()

    with open('country.txt', 'a') as f:
       f.write(" Selected country is : "+ option.text)
       f.write('\n')

    time.sleep(10)
