import xmlrpclib

class Cliente:
    var=''
    def crea(self,puerto=8000,mem='hola',IP='localhost'):
        self.puerto=puerto
        self.s = xmlrpclib.ServerProxy('http://'+IP+':'+str(puerto))
        #lee el mesanje
        self.var=mem
    
    def respuesta(self):
        claro=self.s.men(self.var)
    
        #lo imprime
        return str(self.puerto) +' dice '+str(claro)+'\n'
    
#c=Cliente()        
#c.crea()
#print c.respuesta()
