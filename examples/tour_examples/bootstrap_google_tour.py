from seleniumbase import BaseCase


class MyTourClass(BaseCase):

    def test_google_tour(self):
        self.open('https://google.com')
        self.wait_for_element('input[title="Search"]')

        self.create_bootstrap_tour()  # OR self.create_tour(theme="bootstrap")
        self.add_tour_step(
            "Click to begin the Google Tour!", title="SeleniumBase Tours")
        self.add_tour_step(
            "Type in your search query here.", 'input[title="Search"]')
        self.add_tour_step(
            "Then click here to search!", 'input[value="Google Search"]',
            alignment="bottom")
        self.add_tour_step(
            "Or click here to see the top result.",
            '''[value="I'm Feeling Lucky"]''',
            alignment="bottom")
        self.add_tour_step("Here's an example Google search:")
        self.play_tour()

        self.highlight_update_text('input[title="Search"]', "GitHub")
        self.highlight_click('input[value="Google Search"]')

        self.create_bootstrap_tour()  # OR self.create_tour(theme="bootstrap")
        self.add_tour_step(
            "Search results appear here!", title="(5-second autoplay on)")
        self.add_tour_step("Let's take another tour:")
        self.play_tour(interval=5)  # tour automatically continues after 5 sec

        self.open("https://www.google.com/maps/@42.3598616,-71.0912631,15z")
        self.wait_for_element('input#searchboxinput')

        self.create_bootstrap_tour()  # OR self.create_tour(theme="bootstrap")
        self.add_tour_step("Welcome to Google Maps!")
        self.add_tour_step(
            "Type in a location here.", "#searchboxinput", title="Search Box")
        self.add_tour_step(
            "Then click here to show it on the map.",
            "#searchbox-searchbutton", alignment="bottom")
        self.add_tour_step(
            "Or click here to get driving directions.",
            "#searchbox-directions", alignment="bottom")
        self.add_tour_step(
            "Use this button to switch to Satellite view.",
            "div.widget-minimap", alignment="right")
        self.add_tour_step(
            "Click here to zoom in.", "#widget-zoom-in", alignment="left")
        self.add_tour_step(
            "Or click here to zoom out.", "#widget-zoom-out", alignment="left")
        self.add_tour_step(
            "Use the Menu button to see more options.",
            ".searchbox-hamburger-container", alignment="right")
        self.add_tour_step(
            "Or click here to see more Google apps.", '[title="Google apps"]',
            alignment="left")
        self.add_tour_step(
            "Thanks for trying out SeleniumBase Tours!",
            title="End of Guided Tour")
        self.play_tour()
