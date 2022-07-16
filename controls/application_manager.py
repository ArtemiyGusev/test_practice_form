from selene.support.shared.jquery_style import s


class applicationManager:

    def __init__(self, element_and_element_text):
        self.element_and_element_text = element_and_element_text

    def fill_form(self):
        for element, element_text in self.element_and_element_text.items():
            (s(element)).type(element_text)
