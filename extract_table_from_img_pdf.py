import pdfplumber
import pandas as pd from PIL
import Image
 pdf= pdfplumber.open("warn_report.pdf")
#Load page_0
pØ = pdf.pages [0]
 # Visualize the actual content on page_0
Image.open("page_0.png")

table = p0.extract_table()
df = pd.DataFrame(table[1:], columns=table[0])
for column in ["Effective", "Received"]: df [column] = df[column].str.replace(""
 df.head()
