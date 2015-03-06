
import weakref
from ...testing.unittest_tools import unittest
from ...api import Adapter, Instance, Interface, provides 
from ..api import AdaptationManager, adapt, register_factory


class I(Interface):
    def method(self):
        pass
        
class A(object):
    pass

@provides(I)
class AtoI(Adapter):

    adaptee = Instance(A)
    
    def method(self):
        return u'yey'

register_factory(AtoI, A, I)


class TestWeakproxy(unittest.TestCase):
    def test_allan(self):
        a = A()
        weak_a = weakref.proxy(a)
        i_from_a = adapt(weak_a, I)
        self.assertIsInstance(i_from_a, AtoI)

