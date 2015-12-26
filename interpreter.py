import requests, sys
try:
    f = open(sys.argv[1])
except IOError:
    sys.stderr.write("Could not find file for reading.")
    sys.exit()
except KeyError:
    sys.stderr.write("No file given.")
    sys.exit()
print(requests.get("http://bit.ly/"+f.read()))
