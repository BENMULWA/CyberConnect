from django.core.management.base import BaseCommand
from django.core import signing
from django.contrib.sessions.models import Session

class Command(BaseCommand):
    help = "Decode a short token stored in the session"

    def add_arguments(self, parser):
        parser.add_argument('short_token', type=str, help='The short token to decode (e.g. khm8VRg9b6aMV2NK)')

    def handle(self, *args, **options):
        token = options['short_token']
        session_key = None
        signed_value = None
        decoded_value = None

        # Try to find it in the session store
        sessions = Session.objects.all()
        for session in sessions:
            data = session.get_decoded()
            key = f"token_data_{token}"
            if key in data:
                signed_value = data[key]
                session_key = session.session_key
                break

        if not signed_value:
            self.stdout.write(self.style.ERROR(f"No token_data_{token} found in any session."))
            return

        try:
            decoded_value = signing.loads(signed_value)
        except signing.BadSignature:
            self.stdout.write(self.style.ERROR("Invalid or tampered token signature."))
            return
        except signing.SignatureExpired:
            self.stdout.write(self.style.ERROR("Token has expired."))
            return

        self.stdout.write(self.style.SUCCESS(f"\n✅ Token found in session: {session_key}"))
        self.stdout.write(self.style.SUCCESS("Decoded Token Data:"))
        for key, value in decoded_value.items():
            self.stdout.write(f"  {key}: {value}")
