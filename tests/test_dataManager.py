from src.data_manager import CarregarDadosMinerios

def test_CarregarDadosMinerios():
  
  dados = CarregarDadosMinerios();
  
  assert "metals" in dados
  assert "copper" in dados["metals"]
  assert "native_copper" in dados["metals"]["copper"]["minerals"]
 