class Bottle:
    """
    Die Klasse beschreibt eine Trinkflasche mit den wichtigsten Eigenschaften und Fähigkeiten.
    """

    def __init__(self, color, capacity):
        """
        Erstellt eine leere Flasche mit der durch color angegebenen Farbe und
        der vorgegebene Grösse (capacity).
        :param color:
        :param capacity:
        """
        self.__quantity_avaiable = 0.0  # 0.0 da float
        self.__color = color
        self.__capacity = capacity

    """
    Als Property werden Methoden bezeichnet, die den Wert eines Attributs zurückliefern.
    """
    @property
    def color(self):
        """
        Liefert die Farbe der Flasche
        :return: Farbe der Flasche
        """
        return self.__color

    @property
    def quantity_avaiable(self):
        """
        Liefert die noch verfügbare Mengde an Flüssigkeit.
        :return: verfügbare Menge
        """
        return self.__quantity_avaiable

    @property
    def capacity(self):
        """
        Liefert die Grösse (Kapazität) der Flasche
        :return: Grösse der Flasche
        """
        return self.__capacity

    def open_bottle(self):
        """
        ohne Implementation
        """
        pass

    def close_the_bottle(self):
        """
        ohne Implementation
        """
        pass

    def fill_bottle(self):
        """
        Füllt die Flasche bis sie voll ist.
        """
        self.__quantity_avaiable = self.__capacity

    def get_liquid(self, amount):
        """
        Liefert die durch amount angegeben Menge, sofern diese verfügbar ist.
        Ansonsten wird der Rest des Inhalts geliefert.
        :param amount: gewünschte Menge
        :return: verfügbare Menge
        """
        if amount > self.__quantity_avaiable:
            amount = self.__quantity_avaiable
            self.__quantity_avaiable = 0.0
        else:
            self.__quantity_avaiable -= amount
        return amount