class Fraccion:
    num = 2
    den = 3

    def __init__(self):
        print(self.num)
        print(self.den)

    def imprime(self):
        print(self.num, "/", self.den)


def main():
    print("Main")
    a = Fraccion()  # llama al constructuro
    a.imprime()  # usa el método


class Fraccion2:

    def __init__(self, num, den):
        self.num = num
        self.den = den

    def imprime2(self):
        print(self.num, "/", self.den)


def main2():
    print("Main 2")
    a = Fraccion2(5, 7)  # llama al constructuro
    a.imprime2()  # usa el método


class Fraccion3:

    def __init__(self, num, den):
        self.num = num
        self.den = den

    def imprime3(self):
        print(self.num, "/", self.den)


def main3():
    print("Main 3")
    a = Fraccion3(6, 7)  # llama al constructuro
    a.imprime3()  # usa el método


class Fraccion4:

    def __init__(self, num, den):
        self.num = num
        self.den = den

    def imprime4(self):
        print(self.num, "/", self.den)


def main4():
    print("Main 4")
    a = Fraccion4(6, 7)  # llama al constructuro
    a.imprime4()  # usa el método

    b = Fraccion4(3, 8)
    b.imprime4()


class Fraccion5:
    def __init__(self, num, den):
        self.num = num
        self.den = den

    def imprime5(self):
        print(self.num, "/", self.den)

    def multiplica(self, b):
        print("Main5")
        n = self.num * b.num  # Aqui self es "a"  porque abajo el método lo ejecutó "a"
        d = self.den * b.den
        r = Fraccion5(n, d)
        return r


def main5():
    a = Fraccion5(3, 2)
    b = Fraccion5(7, 4)
    r = a.multiplica(b)
    r.imprime5()


# --------------------------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    main()
    main2()
    main3()
    main4()
    main5()
