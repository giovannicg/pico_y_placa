import pytest
from datetime import datetime
from pico_y_placa import chek_picoyplaca

@pytest.mark.parametrize(
    "placa,fecha,expected",
     [
    ('abc1231', datetime(2022,7,4,9,29,0), True),
    ('abc1239', datetime(2022,7,4,9,29,0), False),
    ('abc1237', datetime(2022,7,7,9,29,0), True),
     ]
)
def test(placa,fecha,expected):
    assert chek_picoyplaca(placa,fecha) == expected
    