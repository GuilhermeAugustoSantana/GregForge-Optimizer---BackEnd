from src.mapear_lista_minerios import mapearListaMinerios

def test_deve_retornar_lista_de_minerios_com_sucesso():
  listaMinerios = mapearListaMinerios();
  
  primeiroMinerio = listaMinerios[0]
  
  assert "id" in primeiroMinerio
  assert "nome" in primeiroMinerio
  assert 'mb' in primeiroMinerio