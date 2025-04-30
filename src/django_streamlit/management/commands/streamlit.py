import subprocess

from django.core.management.base import BaseCommand
from django_streamlit import settings as streamlit_settings


class Command(BaseCommand):
    help = "Run Streamlit app"

    def handle(self, *args, **options):
        """
        Runs `streamlist run app.py` command.

        Allow cancellation with `Ctrl+C`.
        """

        # Run Streamlit app
        subprocess.run(
            [
                "streamlit",
                "run",
                streamlit_settings.STREAMLIT_APP_PATH,
                "--server.port",
                str(streamlit_settings.STREAMLIT_APP_PORT),
            ],
            check=True,
        )
