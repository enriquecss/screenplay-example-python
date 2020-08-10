"""
A very simple Task to give you an idea of what a Task might be or do. An actor
must possess the ability to BrowseTheWeb to perform this task. An actor
performs this task like so:

    the_actor.attempts_to(Start.on_the_homepage())
"""


from screenpy import AnActor
from screenpy.actions import Open

from user_interface import homepage


class Start:
    """
    A very simple task that starts on the ScreenPy docs homepage.
    """

    @staticmethod
    def on_the_homepage() -> "Start":
        """Sets the URL to be the homepage."""
        return Start(homepage.URL)

    def perform_as(self, the_actor: AnActor) -> None:
        """
        Asks the actor to visit the specified URL in their browser.

        Args:
            the_actor: the actor who will perform this task.

        Raises:
            UnableToPerformException: if the actor does not possess the
                ability to BrowseTheWeb.
        """
        the_actor.attempts_to(Open.their_browser_on(self.location))

    def __init__(self, location: str) -> None:
        self.location = location

