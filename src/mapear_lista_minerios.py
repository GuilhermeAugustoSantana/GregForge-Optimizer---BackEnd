from src.data_manager import CarregarDadosMinerios

def mapearListaMinerios():
  dadosMinerios = CarregarDadosMinerios()
  listaFront = []
  
  listaMetais = dadosMinerios.get("metals", {})
  
  for chaveMetal, dadosDoMetal in listaMetais.items():
    
    minerios = dadosDoMetal.get("minerals", {})
    
    for chaveMinerio, conteudo in minerios.items():
      
      dusts = conteudo.get("dusts", {})
      for tipoDust, info in dusts.items():
        listaFront.append({
          "id": f"{chaveMetal}_{chaveMinerio}_dust_{tipoDust}",
          "nome": info["name"],
          "mb": info["mb_value"]
        })
        
      purityLevels = conteudo.get("raw", {}).get("purity_levels", {})
      for nivel, info in purityLevels.items():
        listaFront.append({
          "id": f"{chaveMetal}_{chaveMinerio}_raw_{nivel}",
          "nome": info["name"],
          "mb": info["mb_value"]
        })
        
  return listaFront