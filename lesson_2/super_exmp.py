class A:

    def f(self):
        print('A')


class B(A):

    def f(self):
        print('B')


class C(B):

    def f(self):
        #super(C, self).f() == super().f()
        super(B, self).f()

C().f()