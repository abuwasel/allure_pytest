import pytest

class TestDemoOne:
    @pytest.mark.parametrize('data', [8, 4, 9])
    def test_greater_than_5(self, data):
        if data > 5:
            assert True
        else:
            assert False, 'Given number is less than 5'

class TestDemoTwo:
    @pytest.mark.parametrize('data', [8, 4, 9])
    def test_less_than_5(self, data):
        if data < 5:
            assert True
        else:
            assert False, 'Given number is greater than 5'
