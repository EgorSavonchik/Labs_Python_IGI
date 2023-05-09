
from Serializers.serializers_factory import SerializersFactory, SerializerType


class T:
    A = "asdf"
    B = 11
    C = 14


def my_decorator(func):
    def cwrapper(*args, **kwargs):
        print("start func")
        func(*args, **kwargs)
        print("end func")

    return cwrapper


def for_dec(a):
    print("Hello world", a)


df = my_decorator(for_dec)


class A:
    a = "A"


class B(A):
    a = "B"


class C(A):
    a = "C"


class D(B, C):
    a = "D"

class tesr:
    classmethod
    def clm() :
        return 5

    staticmethod
    def sm() :
        return 4


def decorat(func):
    def wrap(*args):
        if(len(args) >= 10):
            raise("10+")

        func(args)

    return wrap

@decorat
def func(*args) :
    return args.__len__()





if __name__ == '__main__':

    '''o = None
    #o = 103
    #o = {1:{1:{1:{1:{1:{1:{1:1}}}}}}}'''

    s = SerializersFactory.create_serializer(SerializerType.XML)

    with open("data.xml", "w") as file:
        s.dump(A, file)
    with open("data.xml", "r") as file:
        a = s.load(file)

    print(a)
    
    








