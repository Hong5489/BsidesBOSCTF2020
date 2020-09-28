import re
from Crypto.Util.number import long_to_bytes
text = open("dimension_0.html",'r').read()
text = re.findall("<title>(.*)</title>",text)[0]
text = text.replace("Dimension",'').replace(" ",'').replace("0",'')
text = text.replace("\xe2\x80\x8c",'0').replace("\xe2\x80\x8d",'1').replace("\xe2\x80\xac",'2').replace("\xef\xbb\xbf",'3')
print long_to_bytes(int(text+"00",4))[::2]