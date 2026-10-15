import pytest
from process import process

@pytest.mark.wip
@pytest.mark.parametrize('values, esperado', [
    ([2], ['positivo', 'par']),
])

def test_statement_coverage(values, esperado):
    assert process(values) == esperado