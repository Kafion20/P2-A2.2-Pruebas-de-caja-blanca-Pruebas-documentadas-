import pytest
from process import process

@pytest.mark.system
@pytest.mark.parametrize('values, esperado', [
    ([2], ['positivo', 'par']),
])

def test_statement_coverage(values, esperado):
    assert process(values) == esperado




@pytest.mark.system
@pytest.mark.parametrize('values, esperado', [
    ([4], ['positivo', 'par']),   
    ([-3], []),                   
])
def test_ramas(values, esperado):
    assert process(values) == esperado





@pytest.mark.wip
@pytest.mark.parametrize('values, esperado', [
    ([4, 4], ['positivo', 'par', 'positivo', 'par']),   
    ([4, 3], ['positivo', 'par', 'positivo']),          
    ([4, -2], ['positivo', 'par', 'par']),              
    ([4, -1], ['positivo', 'par']),                     
    ([3, 4], ['positivo', 'positivo', 'par']),          
    ([3, 3], ['positivo', 'positivo']),                 
    ([3, -2], ['positivo', 'par']),                     
    ([3, -1], ['positivo']),                            
    ([-2, 4], ['par', 'positivo', 'par']),              
    ([-2, 3], ['par', 'positivo']),                     
    ([-2, -2], ['par', 'par']),                         
    ([-2, -1], ['par']),                                
    ([-1, 4], ['positivo', 'par']),                     
    ([-1, 3], ['positivo']),                            
    ([-1, -2], ['par']),                                
    ([-1, -1], []),                                     
])
def test_caminos(values, esperado):
    assert process(values) == esperado