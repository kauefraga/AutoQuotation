from .getQuotation import getDolarQuotation, getEuroQuotation, getPoundSterlingQuotation, getGoldQuotation, closeBrowser
import pandas as pd

def newQuotationTable():
  dolarQuotation = getDolarQuotation()
  euroQuotation = getEuroQuotation()
  poundSterlingQuotation = getPoundSterlingQuotation()
  goldQuotation = getGoldQuotation()
  closeBrowser()

  table = pd.DataFrame({
    'Moeda':
    [
      'Dólar',
      'Euro',
      'Pound Sterling',
      'Gold'
    ],
    'Cotação':
    [
      dolarQuotation,
      euroQuotation,
      poundSterlingQuotation,
      float(goldQuotation)
    ]
  })

  table.to_csv('../Quotation.csv', index=False)
  return table
