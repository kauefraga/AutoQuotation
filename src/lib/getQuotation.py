from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome('C:/chromedriver/chromedriver.exe', options=options)

def closeBrowser():
  browser.close()

def getDolar():
  browser.get('https://www.google.com.br/search?q=cotacao+dolar')

  dolarQuotation: float = browser.find_element(
    By.XPATH,
    '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]'
  ).get_attribute('data-value')

  return dolarQuotation

def getEuro():
  browser.get('https://www.google.com/search?q=cotacao+euro')

  euroQuotation: float = browser.find_element(
    By.XPATH,
    '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]'
  ).get_attribute('data-value')

  return euroQuotation

def getPoundSterling():
  browser.get('https://www.google.com/search?q=cotacao+libra')

  poundSterlingQuotation: float = browser.find_element(
    By.XPATH,
    '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]'
  ).get_attribute('data-value')

  return poundSterlingQuotation

def getGold():
  browser.get('https://dolarhoje.com/ouro-hoje/')

  goldQuotation: str = browser.find_element(
    By.XPATH,
    '//*[@id="nacional"]'
  ).get_attribute('value')

  return float(goldQuotation.replace(',', '.'))
