
counter_finder = finder.by_semantics_label("counter_semantic")
counter_element = FlutterElement(driver, counter_finder)
print(counter_element.text)
pass
