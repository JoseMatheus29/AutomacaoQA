import os
from utils.driver_factory import get_driver


def before_scenario(context, scenario):
    headless = os.environ.get("HEADLESS", "true").lower() != "false"
    context.driver = get_driver(headless=headless)
    context.product_added = None


def after_scenario(context, scenario):
    if scenario.status == "failed":
        os.makedirs("screenshots", exist_ok=True)
        safe_name = scenario.name.replace(" ", "_").replace("/", "-")
        path = f"screenshots/{safe_name}.png"
        context.driver.save_screenshot(path)
        print(f"\n Evidência salva em: {path}")

    context.driver.quit()
