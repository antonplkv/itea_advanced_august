def a(a_):

    def b(b_):

        def c(c_):

            def d(d_):
                print(a_, b_, c_, d_)

            return d

        return c

    return b



print(a(20)(30)(40)(50))