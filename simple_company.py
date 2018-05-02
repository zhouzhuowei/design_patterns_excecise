# -*- coding:utf-8 -*-

__author__ = 'zzw'

"""
Simple company mode:
   use a class to create other class instance.
   content three part:
        1. a father class
        2. many different method class
        3. a class to create different method instance
create time: 2016.1.31
"""


class FatherClass(object):
    ''' the father class for different method
    '''
    def __init__(self):
        self.num1 = 0
        self.num2 = 0

    def get_result(self):
        pass

''' the different class method '''
class AddOperation(FatherClass):
    ''' for add operation
    '''
    def get_result(self):
        return (self.num1 + self.num2)

class SubOperation(FatherClass):
    ''' for subtraction operation
    '''
    def get_result(self):
        return (self.num1 - self.num2)

class MultiOperation(FatherClass):
    ''' for multiplication operation
    '''
    def get_result(self):
        return (self.num1 * self.num2)

class DivOperation(FatherClass):
    ''' for division operation
    '''
    def get_result(self):
        return (self.num1 / self.num2)

class UndefOperation(FatherClass):
    ''' for undefined case
    '''
    def get_result(self):
        return u'undefined operation!'

''' a class to create different method instance '''
class OperaFactory(object):
    def choose_operation(self, opera):
        if opera == '+':
            return AddOperation()
        elif opera == '-':
            return SubOperation()
        elif opera == '*':
            return MultiOperation()
        elif opera == '/':
            return DivOperation()
        else:
            return UndefOperation()

if __name__ == "__main__":
    num1 = 10
    num2 = 5

    OF = OperaFactory()
    opera_inst = OF.choose_operation('+')
    opera_inst.num1 = num1
    opera_inst.num2 = num2
    print (opera_inst.get_result())
