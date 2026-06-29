# language: pt

Funcionalidade: Fluxo de compra no SauceDemo
  Como um usuário da loja SauceDemo
  Quero realizar o fluxo completo de compra
  Para validar que o sistema funciona corretamente

  Contexto:
    Dado que o usuário acessa o site do SauceDemo

  @positivo @login
  Cenário: Login com credenciais válidas
    Quando o usuário faz login com "standard_user" e senha "secret_sauce"
    Então o usuário deve ser redirecionado para a página de produtos
    E o título da página deve ser "Products"

  @negativo @login
  Esquema do Cenário: Login com credenciais inválidas
    Quando o usuário faz login com "<usuario>" e senha "<senha>"
    Então deve ser exibida a mensagem de erro "<mensagem>"

    Exemplos:
      | usuario          | senha        | mensagem                                                                  |
      | usuario_invalido | secret_sauce | Epic sadface: Username and password do not match any user in this service |
      | standard_user    | senha_errada | Epic sadface: Username and password do not match any user in this service |
      | locked_out_user  | secret_sauce | Epic sadface: Sorry, this user has been locked out.                       |
      | VAZIO            | VAZIO        | Epic sadface: Username is required                                        |

  @positivo @carrinho
  Cenário: Adicionar produto ao carrinho e validar
    Dado que o usuário está logado com "standard_user" e "secret_sauce"
    Quando o usuário adiciona o primeiro produto ao carrinho
    Então o carrinho deve exibir "1" item
    Quando o usuário acessa o carrinho
    Então o produto deve estar listado no carrinho

  @negativo @carrinho
  Cenário: Verificar carrinho vazio
    Dado que o usuário está logado com "standard_user" e "secret_sauce"
    Quando o usuário acessa o carrinho sem adicionar produtos
    Então o carrinho deve estar vazio

  @positivo @compra
  Cenário: Fluxo completo de compra
    Dado que o usuário está logado com "standard_user" e "secret_sauce"
    E o usuário adiciona o primeiro produto ao carrinho
    E o usuário acessa o carrinho
    Quando o usuário prossegue para o checkout
    E o usuário preenche os dados "Joao", "Silva", "60000-000"
    E o usuário finaliza a compra
    Então deve ser exibida a mensagem de sucesso "Thank you for your order!"

  @negativo @checkout
  Cenário: Tentar finalizar checkout sem preencher dados obrigatórios
    Dado que o usuário está logado com "standard_user" e "secret_sauce"
    E o usuário adiciona o primeiro produto ao carrinho
    E o usuário acessa o carrinho
    Quando o usuário prossegue para o checkout
    E o usuário tenta continuar sem preencher os dados
    Então deve ser exibida a mensagem de erro no checkout "Error: First Name is required"
