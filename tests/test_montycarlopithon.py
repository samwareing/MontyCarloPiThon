import pytest

from montycarlopithon import MontyCarloPiThon


class Test_MontyCarloPiThon:

    @pytest.fixture
    def mcpt(self):
        mcpt = MontyCarloPiThon()
        mcpt._set_seed(0)
        return mcpt

    def test_empty_valid(self, mcpt):
        assert mcpt.pi == None
        assert mcpt._hits_in_circle == 0
        assert mcpt._hits_total == 0