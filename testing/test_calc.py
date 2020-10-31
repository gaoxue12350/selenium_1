import pytest
import yaml


def get_datas():
    with open("datas/calc.yml") as f:
        datas = yaml.safe_load(f)
    add_datas = datas['add']['datas']
    add_ids = datas['add']['ids']
    sub_datas = datas['sub']['datas']
    sub_ids = datas['sub']['ids']
    mul_datas = datas['mul']['datas']
    mul_ids = datas['mul']['ids']
    div_datas = datas['div']['datas']
    div_ids = datas['div']['ids']
    print(add_datas, add_ids)
    return [add_datas, add_ids, sub_datas, sub_ids, mul_datas, mul_ids, div_datas, div_ids]


class TestCalc:

    @pytest.mark.run(order=0)
    @pytest.mark.parametrize('a,b,expect', get_datas()[0], ids=get_datas()[1])
    def test_add(self, get_calc, a, b, expect):
        # calc=Calculator()
        result = get_calc.add(a, b)
        assert result == expect

    @pytest.mark.run(order=2)
    @pytest.mark.parametrize('a,b,expect', get_datas()[2], ids=get_datas()[3])
    def test_sub(self, get_calc, a, b, expect):
        # calc=Calculator()
        result = get_calc.sub(a, b)
        assert result == expect

    @pytest.mark.run(order=-1)
    @pytest.mark.parametrize('a,b,expect', get_datas()[4], ids=get_datas()[5])
    def test_mul(self, get_calc, a, b, expect):
        # calc=Calculator()
        result = get_calc.mul(a, b)
        assert result == expect

    @pytest.mark.run(order=1)
    @pytest.mark.parametrize('a,b,expect', get_datas()[6], ids=get_datas()[7])
    def test_div(self, get_calc, a, b, expect):
        result = get_calc.div(a, b)
        assert result == expect
