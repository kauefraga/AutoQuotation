from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome('C:/chromedriver/chromedriver.exe', options=options)

def closeBrowser():
  browser.close()

def getDolarQuotation():
  browser.get('https://www.google.com.br')

  browser.find_element(
    By.XPATH,
    '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div[2]/div[2]/input'
  ).send_keys('Cotação dólar')

  browser.find_element(
    By.XPATH,
    '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div[2]/div[2]/input'
  ).send_keys(Keys.ENTER)

  dolarQuotation: float = browser.find_element(
    By.XPATH,
    '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]'
  ).get_attribute('data-value')

  return dolarQuotation

def getEuroQuotation():
  browser.get('https://www.google.com.br')

  browser.find_element(
    By.XPATH,
    '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div[2]/div[2]/input'
  ).send_keys('Cotação euro')

  browser.find_element(
    By.XPATH,
    '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div[2]/div[2]/input'
  ).send_keys(Keys.ENTER)

  euroQuotation: float = browser.find_element(
    By.XPATH,
    '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]'
  ).get_attribute('data-value')

  return euroQuotation

def getPoundSterlingQuotation():
  browser.get('https://www.google.com.br')

  browser.find_element(
    By.XPATH,
    '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div[2]/div[2]/input'
  ).send_keys('Cotação libra')

  browser.find_element(
    By.XPATH,
    '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div[2]/div[2]/input'
  ).send_keys(Keys.ENTER)

  poundSterlingQuotation: float = browser.find_element(
    By.XPATH,
    '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]'
  ).get_attribute('data-value')

  return poundSterlingQuotation

def getGoldQuotation():
  browser.get('https://dolarhoje.com/ouro-hoje/')

  goldQuotation: str = browser.find_element(
    By.XPATH,
    '//*[@id="nacional"]'
  ).get_attribute('value')

  return float(goldQuotation.replace(',', '.'))
