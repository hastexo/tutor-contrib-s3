import os
from glob import glob

from .__about__ import __version__


HERE = os.path.abspath(os.path.dirname(__file__))

config = {
    "defaults": {
        "VERSION": __version__,
        "HOST": None,
        "PORT": None,
        "REGION": "",
        "USE_SSL": "True",
        "STORAGE_BUCKET": "openedx",
        "FILE_UPLOAD_BUCKET": "{{ S3_STORAGE_BUCKET }}",
        "PROFILE_IMAGE_BUCKET": "{{ S3_STORAGE_BUCKET }}",
        "GRADE_BUCKET": "{{ S3_STORAGE_BUCKET }}",
        "PROFILE_IMAGE_CUSTOM_DOMAIN": None,
        "PROFILE_IMAGE_MAX_AGE": "31536000",
        "ADDRESSING_STYLE": "auto",
        "SIGNATURE_VERSION": "s3v4",
        "CUSTOM_DOMAIN": "",
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
