import re

bds=r"^[0-9]+[a-z]*$"

bds2=r"\d{4,5}\d?$"

res=re.match(bds,'2254dd')
res2=re.match(bds2,'4544')
print(res,res2)