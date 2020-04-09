#language:pt

@web
Funcionalidade: 001 Validar consulta
  Como cliente do sistema
  Desejo consultar um produto
  Para que eu possa analisar e comprar o produto

  @automated
  Cenário: CN01 Consultar pedido com sucesso
    Dado   que estou na tela inicial do marketplace
    Quando no campo de busca informar um parâmetro para consulta
    Então  é apresentado a quantidade dos produtos retornados
    Então  é apresentado os produtos de acordo com o critério buscado


