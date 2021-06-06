import os

from appium.webdriver import Remote
from appium_flutter_finder.flutter_finder import FlutterElement, FlutterFinder

# Example

driver = Remote('http://localhost:4723/wd/hub', dict(
    platformName='iOS',
    automationName='flutter',
    platformVersion='14.4',
    deviceName='iPhone 8',
    app='/Volumes/case-sensitive/references/appium-flutter-driver/example/flutter_app_under_test/build/ios/iphonesimulator/Runner.app'
))

finder = FlutterFinder()

text_finder = finder.by_text('You have pushed the button this many times:')
text_element = FlutterElement(driver, text_finder)

print(text_element.text)

key_finder = finder.by_value_key("next_route_key")
goto_next_route_element = FlutterElement(driver, key_finder)
print(goto_next_route_element.text)
goto_next_route_element.click()

back_finder = finder.page_back()
back_element = FlutterElement(driver, back_finder)
back_element.click()

tooltip_finder = finder.by_tooltip("Increment")
floating_button_element = FlutterElement(driver, tooltip_finder)
floating_button_element.click()

counter_finder = FlutterFinder().by_semantics_label("counter_semantic")
counter_element = FlutterElement(driver, counter_finder)
print(counter_element.text)

finder.by_descendant()
pass


class Flutter:
    def __init__(self, driver) -> None:
        self.driver = driver

    def find_by_text(self, text):
        return FlutterFinder().by_text(self.driver, text)

    def find_by_key(self, key):
        return FlutterFinder().by_value_key(self.driver, key)

flutter = Flutter(driver)
text_element = flutter.find_by_text("You have done")
