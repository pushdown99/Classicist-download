#filename = https://www.classicist.org/pdf/classicist11/docs/Classicist11-2_06.pdf
#
#
#from pathlib import Path
#import requests
#filename = Path('metadata.pdf')
#url = 'http://www.hrecos.org//images/Data/forweb/HRTVBSH.Metadata.pdf'
#response = requests.get(url)
#filename.write_bytes(response.content)

from pathlib import Path
import requests

x = range(1,149)

for n in  x:
  if n < 10:
    idx = "0"+str(n)
  else:
    idx = str(n)

  filename = Path('pdf/{}.pdf'.format(n))
  url = "https://www.classicist.org/pdf/classicist14/docs/Classicist14_complete_singlepage-reduced-2_{}.pdf".format(idx)
  print(url, filename)
  response = requests.get(url)
  filename.write_bytes(response.content)

