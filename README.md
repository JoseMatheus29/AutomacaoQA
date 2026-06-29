# saucedemo-automation

Projeto de automação E2E para o site [SauceDemo](https://www.saucedemo.com/).

![QA Automation](https://github.com/JoseMatheus29/AutomacaoQA/actions/workflows/tests.yml/badge.svg)

---

## Stack

- **Python 3.11**
- **Selenium 4** — automação do browser
- **Behave** — BDD com Gherkin em português
- **Allure** — relatório de execução
- **GitHub Actions** — CI rodando a cada push

---

## Estrutura

```
saucedemo-automation/
├── .github/
│   └── workflows/
│       └── tests.yml
├── features/
│   ├── saucedemo.feature
│   ├── environment.py
│   └── steps/
│       └── steps.py
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
├── utils/
│   └── driver_factory.py
├── behave.ini
└── requirements.txt
```

A camada `pages/` segue o padrão Page Object Model — cada página do site tem sua própria classe com locators e ações. Isso evita duplicação e facilita manutenção quando o seletor de um elemento muda.

Os waits são todos explícitos via `WebDriverWait`. Nenhum `time.sleep` no projeto.

---

## Cenários cobertos

| Cenário | Tipo |
|---|---|
| Login com credenciais válidas | Positivo |
| Login com usuário inválido | Negativo |
| Login com senha incorreta | Negativo |
| Login com usuário bloqueado | Negativo |
| Login com campos vazios | Negativo |
| Adicionar produto e validar carrinho | Positivo |
| Acessar carrinho vazio | Negativo |
| Fluxo completo de compra | Positivo |
| Checkout sem preencher dados obrigatórios | Negativo |

---

## Como rodar

**Pré-requisitos:** Python 3.9+, Google Chrome, Java (para o Allure CLI)

```bash
# instala as dependências
pip install -r requirements.txt

# roda os testes
behave

# roda com relatório Allure
behave -f allure_behave.formatter:AllureFormatter -o reports/allure-results
allure serve reports/allure-results
```

Para rodar com o browser visível:

```bash
HEADLESS=false behave
```

Para rodar só um grupo de testes:

```bash
behave --tags @login
behave --tags @negativo
behave --tags @compra
```

Falhas geram screenshot automático em `screenshots/`.

---

## CI

O pipeline roda via GitHub Actions a cada push na `main`. Os resultados do Allure e os screenshots de falha ficam disponíveis como artefatos na aba Actions do repositório.