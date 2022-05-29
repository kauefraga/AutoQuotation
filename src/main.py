from lib.getQuotation import getDolar, getEuro, getPoundSterling, getGold, closeBrowser
from lib.newTable import newTable

def main():
  dolar = getDolar()
  euro = getEuro()
  poundSterling = getPoundSterling()
  gold = getGold()

  quotationTable = newTable({ dolar, euro, poundSterling, gold })

  print(quotationTable)

  exit()

if __name__ == '__main__':
  main()
