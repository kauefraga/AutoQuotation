import pandas as pd

class newTable:
  def __init__(self, *data):
    self.dolar = data[0]
    self.euro = data[1]
    self.poundSterling = data[2]
    self.gold = data[3]

  def get(self):
    table = pd.DataFrame({
      'Moeda':
      [
        'Dólar',
        'Euro',
        'Libra Esterlina',
        'Ouro'
      ],
      'Cotação':
      [
        self.dolar,
        self.euro,
        self.poundSterling,
        self.gold
      ]
    })

    return table

# def newTable(data):
#   table = pd.DataFrame({
#     'Moeda':
#     [
#       'Dólar',
#       'Euro',
#       'Pound Sterling',
#       'Gold'
#     ],
#     'Cotação':
#     [
#       data.dolarQuotation,
#       data.euroQuotation,
#       data.poundSterlingQuotation,
#       data.goldQuotation
#     ]
#   })

#   return table
