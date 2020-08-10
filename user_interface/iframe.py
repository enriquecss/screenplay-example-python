"""
Locators and URL for the Iframe page.
"""


from screenpy import Target

URLI = "http://the-internet.herokuapp.com/iframe"

IFRAME = Target.the("Iframe").located_by("#mce_0_ifr")
CONTENT = Target.the("The content box").located_by("p")
