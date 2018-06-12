[smtp]
addr={{sender address}}
from={{sender name}}
host={{email host}}
port=25
login={{login, if need auth for host}}
password={{password, if need auth for host}}
delay=1000

[data]
type={{type data storage: json, py (in project csv,xml,db,http-request)}}
path={{path to data file. not use for db,http-request}}
