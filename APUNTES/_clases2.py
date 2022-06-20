class Lampara:
    _ESTADOS_ = ['''
          .
     .    |    ,
      \   '   /
       ` ,-. '
    --- (   ) ---
         \ /
        _|=|_
       |_____|
    ''',
                 '''
         ,-.
        (   )
         \ /
        _|=|_
       |_____|
    ''']

    def __init__(self, esta_encendida):
        self.esta_encendida = esta_encendida

    def muestra_lampara(self):
        if self.esta_encendida == True:
            print(self._ESTADOS_[0])

        else:
            print(self._ESTADOS_[1])

    def encender(self):
        self.esta_encendida = True
        self.muestra_lampara()

    def apagar(self):
        self.esta_encendida = False
        self.muestra_lampara()


def main6():
    a = Lampara(True)
    a.muestra_lampara()


if __name__ == "__main__":
    main6()
