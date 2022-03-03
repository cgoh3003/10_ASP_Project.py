import pandas as pd
import matplotlib.pyplot as plt

class AspProject:


  Country = pd.read_excel('Project_File.xlsx')
  Countrys = (Country.iloc[362:480, 1:16])
  print(Countrys)

  total = pd.DataFrame(Countrys.loc[:].sum())
  print(total)

  total = total.rename(columns={0: 'total'})
  newtotal = total.sort_values(by='total', ascending=False)
  print(newtotal)

  ax = newtotal['total'].plot(kind='bar', title='Amount of peopel travel', figsize=(10, 10), legend=True, fontsize=12)
  myFig = ax.get_figure()
  myFig.savefig('total.png')



