class testClass(object):
    def __init__(self,name):
        self.name = name
        self.__food = None

    # noinspection PyPropertyDefinition
    @property
    def renwu(self):
        print('%s is eating %s'%(self.name,self.__food))
    @renwu.setter
    def renwu(self,food):
        print('set to food',food)
        self.__food = food

a=testClass('wanggang')
a.renwu
a.renwu = '火腿肠'
a.renwu()