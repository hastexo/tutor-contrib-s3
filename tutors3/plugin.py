import os
from glob import glob

from .__about__ import __version__


HERE = os.path.abspath(os.path.dirname(__file__))

config = {
    "defaults": {
        "VERSION": __version__,
        "HOST": "",
        "PORT": "443",
        "USE_SSL": "True",
        "AUTO_CREATE_BUCKET": "True",
        "STORAGE_BUCKET": "openedx",
        "FILE_UPLOAD_BUCKET": "{{ S3_STORAGE_BUCKET }}",
        "COURSE_IMPORT_EXPORT_BUCKET": "{{ S3_STORAGE_BUCKET }}",
        "PROFILE_IMAGE_BUCKET": "{{ S3_STORAGE_BUCKET }}",
        "PROFILE_IMAGE_CUSTOM_DOMAIN": "",
        "PROFILE_IMAGE_MAX_AGE": "31536000",
    },
}


def patches():
    all_patches = {}
    for path in glob(os.path.join(HERE, "patches", "*")):
        with open(path) as patch_file:
            name = os.path.basename(path)
            content = patch_file.read()
            all_patches[name] = content
    return all_patches
