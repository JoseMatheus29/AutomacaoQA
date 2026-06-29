from behave import given, when, then
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def _resolve(value):
    """Converte o placeholder VAZIO em string vazia."""
    return "" if value == "VAZIO" else value


# ──────────────────────────────────────────────
#  CONTEXTO / SETUP
# ──────────────────────────────────────────────

@given("que o usuário acessa o site do SauceDemo")
def step_open_site(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.open()


@given('que o usuário está logado com "{username}" e "{password}"')
def step_already_logged_in(context, username, password):
    context.login_page = LoginPage(context.driver)
    context.login_page.open()
    context.login_page.login(username, password)
    context.inventory_page = InventoryPage(context.driver)
    assert context.inventory_page.is_on_inventory_page(), \
        "Login falhou: usuário não foi redirecionado para a página de produtos."


# ──────────────────────────────────────────────
#  LOGIN – POSITIVO
# ──────────────────────────────────────────────

@when('o usuário faz login com "{username}" e senha "{password}"')
def step_do_login(context, username, password):
    context.login_page = LoginPage(context.driver)
    context.login_page.login(_resolve(username), _resolve(password))


@then("o usuário deve ser redirecionado para a página de produtos")
def step_check_redirect_to_inventory(context):
    context.inventory_page = InventoryPage(context.driver)
    assert context.inventory_page.is_on_inventory_page(), \
        f"URL atual: {context.driver.current_url} — esperava conter 'inventory'."


@then('o título da página deve ser "{expected_title}"')
def step_check_page_title(context, expected_title):
    actual = context.inventory_page.get_page_title()
    assert actual == expected_title, \
        f"Título esperado: '{expected_title}', obtido: '{actual}'."


# ──────────────────────────────────────────────
#  LOGIN – NEGATIVO
# ──────────────────────────────────────────────

@then('deve ser exibida a mensagem de erro "{expected_message}"')
def step_check_login_error(context, expected_message):
    context.login_page = LoginPage(context.driver)
    assert context.login_page.has_error(), \
        "Nenhuma mensagem de erro foi exibida na tela de login."
    actual = context.login_page.get_error_message()
    assert actual == expected_message, \
        f"Mensagem esperada: '{expected_message}'\nMensagem obtida:   '{actual}'"


# ──────────────────────────────────────────────
#  CARRINHO
# ──────────────────────────────────────────────

@when("o usuário adiciona o primeiro produto ao carrinho")
@given("o usuário adiciona o primeiro produto ao carrinho")
def step_add_first_product(context):
    context.inventory_page = InventoryPage(context.driver)
    context.product_added = context.inventory_page.add_first_product_to_cart()


@then('o carrinho deve exibir "{count}" item')
def step_check_cart_badge(context, count):
    actual = context.inventory_page.get_cart_count()
    assert actual == count, \
        f"Badge do carrinho esperado: '{count}', obtido: '{actual}'."


@when("o usuário acessa o carrinho")
@given("o usuário acessa o carrinho")
def step_go_to_cart(context):
    context.inventory_page = InventoryPage(context.driver)
    context.inventory_page.go_to_cart()
    context.cart_page = CartPage(context.driver)


@then("o produto deve estar listado no carrinho")
def step_check_product_in_cart(context):
    assert context.cart_page.is_on_cart_page(), \
        "Não está na página do carrinho."
    assert context.product_added is not None, \
        "Nenhum produto foi registrado como adicionado."
    assert context.cart_page.has_product(context.product_added), \
        f"Produto '{context.product_added}' não encontrado no carrinho."


@when("o usuário acessa o carrinho sem adicionar produtos")
def step_go_to_cart_empty(context):
    context.inventory_page = InventoryPage(context.driver)
    context.inventory_page.go_to_cart()
    context.cart_page = CartPage(context.driver)


@then("o carrinho deve estar vazio")
def step_check_empty_cart(context):
    assert context.cart_page.is_cart_empty(), \
        f"Esperava carrinho vazio, mas encontrou {context.cart_page.get_item_count()} item(ns)."


# ──────────────────────────────────────────────
#  CHECKOUT
# ──────────────────────────────────────────────

@when("o usuário prossegue para o checkout")
def step_go_to_checkout(context):
    context.cart_page = CartPage(context.driver)
    context.cart_page.go_to_checkout()
    context.checkout_page = CheckoutPage(context.driver)


@when('o usuário preenche os dados "{first_name}", "{last_name}", "{postal_code}"')
def step_fill_checkout_info(context, first_name, last_name, postal_code):
    context.checkout_page = CheckoutPage(context.driver)
    context.checkout_page.fill_personal_info(first_name, last_name, postal_code)


@when("o usuário tenta continuar sem preencher os dados")
def step_continue_without_data(context):
    context.checkout_page = CheckoutPage(context.driver)
    context.checkout_page.fill_personal_info("", "", "")


@when("o usuário finaliza a compra")
def step_finish_purchase(context):
    context.checkout_page = CheckoutPage(context.driver)
    context.checkout_page.finish_purchase()


@then('deve ser exibida a mensagem de sucesso "{expected_message}"')
def step_check_success_message(context, expected_message):
    assert context.checkout_page.is_purchase_complete(), \
        "A mensagem de sucesso não foi encontrada na página."
    actual = context.checkout_page.get_success_header()
    assert actual == expected_message, \
        f"Mensagem de sucesso esperada: '{expected_message}'\nObtida: '{actual}'"


@then('deve ser exibida a mensagem de erro no checkout "{expected_message}"')
def step_check_checkout_error(context, expected_message):
    assert context.checkout_page.has_error(), \
        "Nenhuma mensagem de erro foi exibida no checkout."
    actual = context.checkout_page.get_error_message()
    assert actual == expected_message, \
        f"Mensagem esperada: '{expected_message}'\nObtida: '{actual}'"
