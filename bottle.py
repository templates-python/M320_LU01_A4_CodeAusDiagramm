class Bottle:
    '''
    fügen Sie hier als Erstes den Konstruktor ein.
    '''

    def __init__(self, color, capacity):
        """
        Erstellt eine leere Flasche mit der durch color angegebenen Farbe und
        der vorgegebene Grösse (capacity).
        :param color:
        :param capacity:
        """
        self._quantity_available = 0.0  # 0.0 da float
        self._color = color
        self._capacity = capacity

    '''
    Erstellen Sie der Reihe nach die 3 getter-Methoden.
    Verwenden Sie den Decorator @property.
    '''

    @property
    def color(self):
        """
        Liefert die Farbe der Flasche
        :return: Farbe der Flasche
        """
        return self._color

    @property
    def quantity_available(self):
        """
        Liefert die noch verfügbare Mengde an Flüssigkeit.
        :return: verfügbare Menge
        """
        return self._quantity_available

    @property
    def capacity(self):
        """
        Liefert die Grösse (Kapazität) der Flasche
        :return: Grösse der Flasche
        """
        return self._capacity

    '''
    Erstellen Sie der Reihe nach die restlichen 4 Methoden.
    '''
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
        self._quantity_available = self._capacity

    def get_liquid(self, amount):
        """
        Liefert die durch amount angegeben Menge, sofern diese verfügbar ist.
        Ansonsten wird der Rest des Inhalts geliefert.
        :param amount: gewünschte Menge
        :return: verfügbare Menge
        """
        if amount > self._quantity_available:
            amount = self._quantity_available
            self._quantity_available = 0.0
        else:
            self._quantity_available -= amount
        return amount
