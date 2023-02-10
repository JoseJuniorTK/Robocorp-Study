from RPA.Browser import Browser
from RPA.FileSystem import FileSystem
from RPA.Desktop.Windows import Desktop

browser = Browser()
desktop = Desktop()

def store_web_page_content():
    browser.open_available_browser("https://www.nytimes.com", maximized=True)
    browser.click_element_when_visible('xpath://button[@class="css-aovwtd"]')
    desktop.click('ocr:"Politics"')
    browser.click_element_when_visible('//li[@data-testid="mini-nav-item"]/a[text()="Politics"]')
    text = browser.get_text("css:body")
    FileSystem().create_file("output/text.txt", text, overwrite=True)


def main():
    try:
        store_web_page_content()
    finally:
        browser.close_browser()


if __name__ == "__main__":
    main()
