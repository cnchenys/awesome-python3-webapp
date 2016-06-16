from wsgiref.simple_server import make_server

from hellow import application

httpd = make_server('',9100,application)
print('server did start')
httpd.serve_forever()