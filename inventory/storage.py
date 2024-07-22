from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os

class CustomFileSystemStorage(FileSystemStorage):
    def __init__(self, location=settings.MEDIA_ROOT, base_url=settings.MEDIA_URL):
        super().__init__(location, base_url)

    def get_available_name(self, name, max_length=None):
        # This will ensure that the uploaded file has a unique name
        if self.exists(name):
            base, ext = os.path.splitext(name)
            counter = 1
            while self.exists(name):
                name = f"{base}_{counter}{ext}"
                counter += 1
        return name
