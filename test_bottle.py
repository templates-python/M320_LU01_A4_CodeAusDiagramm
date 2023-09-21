import pytest
from bottle import Bottle


class TestBottle:

    @pytest.fixture
    def bottle(self):
        return Bottle('blue', 1000)

    def test_bottle_initialisation(self, bottle):
        assert bottle.color == 'blue'
        assert bottle.capacity == 1000
        assert bottle.quantity_available == 0

    def test_fill_bottle(self, bottle):
        bottle.fill_bottle()
        assert bottle.quantity_available == bottle.capacity

    def test_get_liquid_well(self, bottle):
        bottle.fill_bottle()
        bottle.get_liquid(500)
        assert bottle.quantity_available == 500

    def test_get_liquid_ugly(self, bottle):
        bottle.fill_bottle()
        amount = bottle.get_liquid(1500)
        assert amount == bottle.capacity
        assert bottle.quantity_available == 0
