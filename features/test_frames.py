"""
An example of a test module that follows the typical unittest.TestCase
test structure. These tests exercise the frame switching actions.
"""


import unittest

from screenpy import AnActor, given, then, when
from screenpy.abilities import BrowseTheWeb
from screenpy.actions import Open, SwitchTo
from screenpy.pacing import act, scene
from screenpy.questions import Text
from screenpy.resolutions import ReadsExactly
from tasks import start

from user_interface.homepage import URL
from user_interface.iframe import CONTENT, URLI, IFRAME


class TestFrames(unittest.TestCase):

    def setUp(self):
        self.actor = AnActor.named("Anton").who_can(BrowseTheWeb.using_firefox())

    @act("Perform")
    @scene("SwitchToIframe")
    def test_switch_to_iframe(self):
    
        Anton = self.actor

        given(Anton).was_able_to(Open.their_browser_on(URL))
        given(Anton).attempts_to(Open.their_browser_on(URLI))
        when(Anton).attempts_to(SwitchTo.the(IFRAME))
        then(Anton).should_see_the(
            (Text.of_the(CONTENT), ReadsExactly("Your content goes here."))
        )

    def tearDown(self):
        self.actor.exit()
