import time

from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError

# Constants
TARGET_WIDTH = 219.4
TARGET_HEIGHT = 40
TOLERANCE = 0.5

def is_within_tolerance(actual, expected, tolerance):
    return abs(actual - expected) <= tolerance

def check_input_box_size(selector, page):
    locator = page.locator(selector)
    locator.wait_for(state="visible")
    box = locator.bounding_box()

    print(f"Checking: {selector}")
    print(f"→ Width: {box['width']:.2f}px | Height: {box['height']:.2f}px")

    assert is_within_tolerance(box['width'], TARGET_WIDTH, TOLERANCE), f"Width out of range: {box['width']}px"
    assert is_within_tolerance(box['height'], TARGET_HEIGHT, TOLERANCE), f"Height out of range: {box['height']}px"

    print("✅ Passed tolerance check.\n")

def test_all_input_boxes():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        #page.goto("https://flatandvilla.com/العاصمة-الإدارية-الجديدة")
        page.goto("https://flatandvilla.com/القاهرة-الجديدة")
        #page.goto("https://flatandvilla.com/الساحل-الشمالي")
        #page.goto("https://flatandvilla.com/6-اكتوبر")
        #page.goto("https://flatandvilla.com/الغردقة")
        #page.goto("https://flatandvilla.com/الشيخ-زايد")
        #page.goto("https://flatandvilla.com/العين-السخنة")

        links=page.query_selector_all(".elementor-heading-title.elementor-size-small")
        counter = 0
        for i in range(3):

            try:
                if i > 0:  # Start from index 1 (index 0 is already handled)
                   # page.goto("https://flatandvilla.com/العاصمة-الإدارية-الجديدة")
                    page.goto("https://flatandvilla.com/القاهرة-الجديدة")
                   # page.goto("https://flatandvilla.com/الساحل-الشمالي")
                   # page.goto("https://flatandvilla.com/6-اكتوبر")
                   # page.goto("https://flatandvilla.com/الغردقة")
                   # page.goto("https://flatandvilla.com/الشيخ-زايد")
                   # page.goto("https://flatandvilla.com/العين-السخنة")
                    links = page.query_selector_all(
                        ".elementor-heading-title.elementor-size-small")  # Re-query links after loading
                    links[i].click()
                else:
                    links[i].click()
                locator = page.locator("#form-field-name_sidebar")
                locator.wait_for(state="visible")
                box = locator.bounding_box()
                assert is_within_tolerance(box['width'], TARGET_WIDTH, TOLERANCE), f"Width out of range: {box['width']}px"
                assert is_within_tolerance(box['height'], TARGET_HEIGHT, TOLERANCE), f"Height out of range: {box['height']}px"
                print("***************************************************done**********************************")
            except PlaywrightTimeoutError:
                print(f"⚠️ Timeout occurred while processing link {i}, skipping to next link.")
                continue  # Skip to the next link if a timeout occurs

        browser.close()





