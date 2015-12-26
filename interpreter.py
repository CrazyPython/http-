import requests, sys
try:
    f = open(sys.argv[2])
except IOError:
    sys.stderr.write("Could not find file for reading.")
    sys.exit()
print(requests.get("http://bit.ly/"+f.read()))
