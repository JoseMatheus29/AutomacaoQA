import os
import glob
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


def _resolve_chromedriver_path():
    """
    No CI (GitHub Actions), usa o chromedriver instalado pela action setup-chrome.
    Localmente, usa o webdriver-manager com correção do bug de path.
    """

    ci_path = os.environ.get("CHROMEDRIVER_PATH")
    if ci_path and os.path.isfile(ci_path):
        return ci_path

    from webdriver_manager.chrome import ChromeDriverManager

    raw_path = ChromeDriverManager().install()

    if os.path.isfile(raw_path) and not raw_path.endswith(".chromedriver"):
        return raw_path

    search_dir = raw_path
    for _ in range(4):
        search_dir = os.path.dirname(search_dir)
        for name in ("chromedriver.exe", "chromedriver"):
            matches = glob.glob(
                os.path.join(search_dir, "**", name), recursive=True
            )
            matches = [m for m in matches if not m.endswith(".chromedriver")]
            if matches:
                return matches[0]

    raise FileNotFoundError(
        f"chromedriver não encontrado.\n"
        f"Caminho retornado pelo webdriver-manager: {raw_path}\n"
        f"Tente deletar a pasta ~/.wdm e rodar novamente."
    )


def get_driver(headless=True):
    """Cria e retorna uma instância do Chrome WebDriver."""
    options = Options()

    if headless:
        options.add_argument("--headless=new")

    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-popup-blocking")

    driver_path = _resolve_chromedriver_path()
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(0)
    return driver