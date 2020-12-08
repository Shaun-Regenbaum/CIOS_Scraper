from bs4 import BeautifulSoup
import requests

addr = "https://wwwh.smartevals.com/Reporting/Students/Wizard.aspx?Type=Classes"

r = requests.get(addr)

print(r.status_code)

soup = BeautifulSoup(r.text, 'lxml')
print(soup)
print(str(soup.find(id= "_ctl0_cphContent_grd1_DXDataRow0")))