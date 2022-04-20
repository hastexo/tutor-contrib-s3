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

    pip install git+https://github.com/hastexo/tutor-contrib-s3@v0.2.1

Then, to enable this plugin, run:

    tutor plugins enable s3

Configuration
-------------

* `OPENEDX_AWS_ACCESS_KEY` (default: `""`)
* `OPENEDX_AWS_SECRET_ACCESS_KEY` (default: `""`)
* `S3_HOST` (default: `""`) - set only if using any other service than AWS S3
* `S3_PORT` (default: `""`) - set only if using any other service than AWS S3
* `S3_REGION` (default: `""`)
* `S3_USE_SSL` (default: `true`)
* `S3_STORAGE_BUCKET` (default: `"openedx"`)
* `S3_FILE_UPLOAD_BUCKET` (default: `"{{ S3_STORAGE_BUCKET }}"`)
* `S3_PROFILE_IMAGE_BUCKET` (default: `"{{ S3_STORAGE_BUCKET }}"`)
* `S3_GRADE_BUCKET` (default: `"{{ S3_STORAGE_BUCKET }}"`)
* `S3_ADDRESSING_STYLE` (default: `"auto"`)
* `S3_SIGNATURE_VERSION` (default: `"s3v4"`)
* `S3_CUSTOM_DOMAIN` (default: `""`) - do not set if you are using AWS S3
* `S3_PROFILE_IMAGE_CUSTOM_DOMAIN` (default: `""`)

These values can be modified with `tutor config save --set
PARAM_NAME=VALUE` commands.

Depending on the nature and configuration of your S3-compatible
service, some of these values may be required to set.

* If using AWS S3, you will need to set `S3_REGION` to a non-empty value. 
  And make sure `S3_ADDRESSING_STYLE` is set to `"auto"` (default) and 
  `S3_CUSTOM_DOMAIN` is set to `""` (default).
* If you want to use an alternative S3-compatible service, you need to set the 
  `S3_HOST` and `S3_PORT` parameters.
* For a Ceph Object Gateway that doesn’t set
  [rgw_dns_name](https://docs.ceph.com/en/latest/radosgw/config-ref/#confval-rgw_dns_name),
  you will need `S3_ADDRESSING_STYLE: path`.
* Due to limitations in Open edX, if you are using `s3v4` signatures, your 
  `S3_PROFILE_IMAGE_BUCKET` must have a public ACL and you must set 
  `S3_PROFILE_IMAGE_CUSTOM_DOMAIN`.
