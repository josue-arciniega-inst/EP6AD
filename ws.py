import cherrypy
import pandas as pd
import myprocessor
import json
p = myprocessor.MyProcessor()

class MyWebService(object):

   @cherrypy.expose
   @cherrypy.tools.json_out()
   @cherrypy.tools.json_in()
   def sum(self):
      data = cherrypy.request.json
      out = p.suma(data['a'],data['b'])
      return json.dumps({'r':out})
   @cherrypy.expose
   @cherrypy.tools.json_out()
   @cherrypy.tools.json_in()
   def res(self):
      data = cherrypy.request.json
      out = p.resta(data['a'],data['b'])
      return json.dumps({'r':out})
   @cherrypy.expose
   @cherrypy.tools.json_out()
   @cherrypy.tools.json_in()
   def mul(self):
      data = cherrypy.request.json
      out = p.multiplica(data['a'],data['b'])
      return json.dumps({'r':out})
   @cherrypy.expose
   @cherrypy.tools.json_out()
   @cherrypy.tools.json_in()
   def div(self):
      data = cherrypy.request.json
      out = p.divide(data['a'],data['b'])
      return json.dumps({'r':out})
   @cherrypy.expose
   @cherrypy.tools.json_out()
   @cherrypy.tools.json_in()
   def calc(self):
      data = cherrypy.request.json
      r=0
      if (data['op']=='sum'):
         r=p.suma(data['a'],data['b'])
      elif (data['op']=='res'):
         r=p.resta(data['a'],data['b'])
      elif (data['op']=='mul'):
         r=p.multiplica(data['a'],data['b'])
      elif (data['op']=='div'):
         r=p.divide(data['a'],data['b'])
      else:
          return json.dumps({'r':'Checa tu op :V','status':0})   
      return json.dumps({'r':r,'status':1})

if __name__ == '__main__':
   config = {'server.socket_host': '0.0.0.0'}
   cherrypy.config.update(config)
   cherrypy.quickstart(MyWebService())
