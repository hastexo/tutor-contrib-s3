Object storage for Open edX with S3
===================================

This is an **experimental** plugin for
[Tutor](https://docs.tutor.overhang.io) that allows Open edX to be
configured with custom S3 settings, including the use of an S3
API-compatible storage platform — such as [Ceph with
radosgw](https://docs.ceph.com/en/latest/radosgw/index.html).

This plugin is meant to make Tutor-managed Open edX interface with S3
*hosted outside of Tutor.* If instead you want to deploy your own
S3-compatible storage platform *as part of Tutor,* please consider the
[minio](https://github.com/overhangio/tutor-minio) Tutor plugin.

Installation
------------

    pip install tutor-contrib-s3

Then, to enable this plugin, run::

    tutor plugins enable s3

Configuration
-------------

* `OPENEDX_AWS_ACCESS_KEY` (default: `""`)
* `OPENEDX_AWS_SECRET_ACCESS_KEY` (default: `""`)
* `S3_HOST` (default: `"s3.amazonaws.com"`)
* `S3_PORT` (default: `443`)
* `S3_USE_SSL` (default: `"True"`)
* `S3_STORAGE_BUCKET` (default: `"openedx"`)
* `S3_FILE_UPLOAD_BUCKET` (default: `"{{ S3_STORAGE_BUCKET }}"`)
* `S3_COURSE_IMPORT_EXPORT_BUCKET` (default: `"{{ S3_STORAGE_BUCKET }}"`)
* `S3_PROFILE_IMAGE_BUCKET` (default: `"{{ S3_STORAGE_BUCKET }}"`)
* `S3_GRADE_BUCKET` (default: `"{{ S3_STORAGE_BUCKET }}"`)
* `S3_PROFILE_IMAGE_CUSTOM_DOMAIN` (default: `""`)
* `S3_PROFILE_IMAGE_MAX_AGE` (default: `31536000`)
* `S3_ADDRESSING_STYLE` (default: `virtual`)
* `S3_SIGNATURE_VERSION` (default: `s3v4`)

These values can be modified with `tutor config save --set
PARAM_NAME=VALUE` commands.
