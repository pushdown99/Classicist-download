from pathlib import Path
from PyPDF2 import PdfFileMerger

x = range(1,149)

merger = PdfFileMerger()

for n in  x:
  if n < 10:
    idx = "0"+str(n)
  else:
    idx = str(n)

  filename = Path('pdf/{}.pdf'.format(n))
  merger.append(filename)

merger.write("Classicist.No14.pdf")
merger.close()
