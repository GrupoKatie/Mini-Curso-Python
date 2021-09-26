
    @property
    def func(self):
        return self.func

    #é equivalente a:

    def func(self):
        return self._func

    func = property(func)
