#hesablayici lahiyehesi(calculator project)
#class Hesablayici --> init(constructor)----->method/atribute ----> function yada method

class Hesablayici(object):
    #init methodu
    def __init__(self,a,b):
        #atributlar
        self.deyer1=a
        self.deyer2=b

    #toplama(adding)
    def toplama(self):
        return self.deyer1+self.deyer2

    def vurma(self):
        "vurma"
        return self.deyer1*self.deyer2


#global deyerler
secin='sece bilersiz'
daxiledin='Zehmet olmasa reqemi daxil edin:'
sec=int(input('Tplama ucun--1'+'  '+secin+'  '+ 'Vurma ucun--2'+secin))
d1=int(input(daxiledin))
d2=int(input(daxiledin))
emeliyyat=Hesablayici(d1,d2)
cavab=emeliyyat

if sec == 1:
    toplama_emeliyyati=emeliyyat.toplama()
    print ("Topla:{}".format(toplama_emeliyyati))
else:

    vurma_emeliyyati=emeliyyat.vurma()
    print ("Vurma:{}".format(vurma_emeliyyati))
