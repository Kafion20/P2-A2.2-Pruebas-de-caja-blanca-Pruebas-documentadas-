import pytest
from process import process

@pytest.mark.system
@pytest.mark.parametrize('values, esperado', [
    ([2], ['positivo', 'par']),
])

def test_statement_coverage(values, esperado):
    assert process(values) == esperado




@pytest.mark.wip
@pytest.mark.parametrize('values, esperado', [
    ([4], ['positivo', 'par']),   
    ([-3], []),                   
])
def test_ramas(values, esperado):
    assert process(values) == esperado