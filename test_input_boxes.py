import time
import requests  # <--- Add this import

from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError

# Slack webhook setup
SLACK_WEBHOOK_URL = "https://hooks.slack.com/services/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"  # <-- Change this!

def send_slack_message(message):
    payload = {"text": message}
    try:
        requests.post(SLACK_WEBHOOK_URL, json=payload)
    except Exception as e:
        print(f"Error sending message to Slack: {e}")

# Constants
TARGET_WIDTH = 219.4
TARGET_HEIGHT = 40
TOLERANCE = 0.5
HOME_TARGET_WIDTH = 188.0
HOME_TARGET_HEIGHT = 40.0
HOME_TOLERANCE = 0.5
def is_within_tolerance(actual, expected, tolerance):
    return abs(actual - expected) <= tolerance



def test_all_input_boxes_tagmo3():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
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
        for i in range(2):
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
                try:
                    assert is_within_tolerance(box['width'], TARGET_WIDTH, TOLERANCE), f"Width out of range: {box['width']}px"
                    assert is_within_tolerance(box['height'], TARGET_HEIGHT, TOLERANCE), f"Height out of range: {box['height']}px"
                    print("***************************************************done in tagmo3**********************************")
                except AssertionError as e:
                    msg = f":x: Assertion failed in تجمع"
                    print(msg)
                    #send_slack_message(msg)
                    raise
            except PlaywrightTimeoutError:
                print(f"⚠️ Timeout occurred while processing link {i}, skipping to next link.")
                continue  # Skip to the next link if a timeout occurs

        browser.close()
def test_all_input_boxes_3asema():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto("https://flatandvilla.com/العاصمة-الإدارية-الجديدة")
        #page.goto("https://flatandvilla.com/القاهرة-الجديدة")
        #page.goto("https://flatandvilla.com/الساحل-الشمالي")
        #page.goto("https://flatandvilla.com/6-اكتوبر")
        #page.goto("https://flatandvilla.com/الغردقة")
        #page.goto("https://flatandvilla.com/الشيخ-زايد")
        #page.goto("https://flatandvilla.com/العين-السخنة")

        links=page.query_selector_all(".elementor-heading-title.elementor-size-small")
        counter = 0
        for i in range(2):
            try:
                if i > 0:  # Start from index 1 (index 0 is already handled)
                    page.goto("https://flatandvilla.com/العاصمة-الإدارية-الجديدة")
                    #page.goto("https://flatandvilla.com/القاهرة-الجديدة")
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
                try:
                    assert is_within_tolerance(box['width'], TARGET_WIDTH, TOLERANCE), f"Width out of range: {box['width']}px"
                    assert is_within_tolerance(box['height'], TARGET_HEIGHT, TOLERANCE), f"Height out of range: {box['height']}px"
                    print("***************************************************done in 3asema**********************************")
                except AssertionError as e:
                    msg = f":x: Assertion failed in تجمع"
                    print(msg)
                    send_slack_message(msg)
                    raise
            except PlaywrightTimeoutError:
                print(f"⚠️ Timeout occurred while processing link {i}, skipping to next link.")
                continue  # Skip to the next link if a timeout occurs

        browser.close()
def test_all_input_boxes_sahel():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        #page.goto("https://flatandvilla.com/العاصمة-الإدارية-الجديدة")
        #page.goto("https://flatandvilla.com/القاهرة-الجديدة")
        page.goto("https://flatandvilla.com/الساحل-الشمالي")
        #page.goto("https://flatandvilla.com/6-اكتوبر")
        #page.goto("https://flatandvilla.com/الغردقة")
        #page.goto("https://flatandvilla.com/الشيخ-زايد")
        #page.goto("https://flatandvilla.com/العين-السخنة")

        links=page.query_selector_all(".elementor-heading-title.elementor-size-small")
        counter = 0
        for i in range(2):
            try:
                if i > 0:  # Start from index 1 (index 0 is already handled)
                   # page.goto("https://flatandvilla.com/العاصمة-الإدارية-الجديدة")
                    #page.goto("https://flatandvilla.com/القاهرة-الجديدة")
                    page.goto("https://flatandvilla.com/الساحل-الشمالي")
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
                try:
                    assert is_within_tolerance(box['width'], TARGET_WIDTH, TOLERANCE), f"Width out of range: {box['width']}px"
                    assert is_within_tolerance(box['height'], TARGET_HEIGHT, TOLERANCE), f"Height out of range: {box['height']}px"
                    print("***************************************************done in sahel**********************************")
                except AssertionError as e:
                    msg = f":x: Assertion failed in sahel"
                    print(msg)
                    send_slack_message(msg)
                    raise
            except PlaywrightTimeoutError:
                print(f"⚠️ Timeout occurred while processing link {i}, skipping to next link.")
                continue  # Skip to the next link if a timeout occurs

        browser.close()
def test_all_input_boxes_october():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        #page.goto("https://flatandvilla.com/العاصمة-الإدارية-الجديدة")
        #page.goto("https://flatandvilla.com/القاهرة-الجديدة")
        #page.goto("https://flatandvilla.com/الساحل-الشمالي")
        page.goto("https://flatandvilla.com/6-اكتوبر")
        #page.goto("https://flatandvilla.com/الغردقة")
        #page.goto("https://flatandvilla.com/الشيخ-زايد")
        #page.goto("https://flatandvilla.com/العين-السخنة")

        links=page.query_selector_all(".elementor-heading-title.elementor-size-small")
        counter = 0
        for i in range(2):
            try:
                if i > 0:  # Start from index 1 (index 0 is already handled)
                   # page.goto("https://flatandvilla.com/العاصمة-الإدارية-الجديدة")
                    #page.goto("https://flatandvilla.com/القاهرة-الجديدة")
                   # page.goto("https://flatandvilla.com/الساحل-الشمالي")
                    page.goto("https://flatandvilla.com/6-اكتوبر")
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
                print(box)
                try:
                    assert is_within_tolerance(box['width'], TARGET_WIDTH, TOLERANCE), f"Width out of range: {box['width']}px"
                    assert is_within_tolerance(box['height'], TARGET_HEIGHT, TOLERANCE), f"Height out of range: {box['height']}px"
                    print("***************************************************done**********************************")
                except AssertionError as e:
                    msg = f":x: Assertion failed in october"
                    print(msg)
                    send_slack_message(msg)
                    raise
            except PlaywrightTimeoutError:
                print(f"⚠️ Timeout occurred while processing link {i}, skipping to next link.")
                continue  # Skip to the next link if a timeout occurs

        browser.close()

def test_home_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context=browser.new_context()
        page = context.new_page()
        page.goto("https://flatandvilla.com/")
        page.mouse.wheel(0, 1000)

        locator = page.locator("#form-field-name_sidebar")
        locator.wait_for(state="visible")
        box = locator.bounding_box()
        print(box)
        try:
            assert is_within_tolerance(box['width'], HOME_TARGET_WIDTH, 0.5), f"Width out of range: {box['width']}px"
            assert is_within_tolerance(box['height'], HOME_TARGET_HEIGHT,
                                       0.5), f"Height out of range: {box['height']}px"
            print("***************************************************done in home page**********************************")
        except AssertionError as e:
            msg = f":x: Assertion failed in Home page"
            print(msg)
            send_slack_message(msg)

def test_slack():
     msg = f"last test"
     print(msg)
     send_slack_message(msg)    

