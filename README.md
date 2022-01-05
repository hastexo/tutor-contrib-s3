Object storage for Open edX with S3
===================================

This is a **experimental** plugin for
[Tutor](https://docs.tutor.overhang.io) that allows Open edX to be
configured to use a custom S3 host.

**Do not use this plugin in production Tutor/Open edX environment.**

Installation
------------

    pip install tutor-s3

Then, to enable this plugin, run::

    tutor plugins enable s3

Configuration
-------------

* `OPENEDX_AWS_ACCESS_KEY` (default: `""`)
* `OPENEDX_AWS_SECRET_ACCESS_KEY` (default: `""`)
* `S3_HOST` (default: `""`)
* `S3_PORT` (default: `443`)
* `S3_USE_SSL` (default: `"True"`)
* `S3_AUTO_CREATE_BUCKET` (default: `"True"`)
* `S3_STORAGE_BUCKET` (default: `"openedx"`)
* `S3_FILE_UPLOAD_BUCKET` (default: `"{{ S3_STORAGE_BUCKET }}"`)
* `S3_COURSE_IMPORT_EXPORT_BUCKET` (default:
    `"{{ S3_STORAGE_BUCKET }}"`)
* `S3_PROFILE_IMAGE_BUCKET` (default: `"{{ S3_STORAGE_BUCKET }}"`)
* `S3_PROFILE_IMAGE_CUSTOM_DOMAIN` (default: `""`)
* `S3_PROFILE_IMAGE_MAX_AGE` (default: `31536000`)

These values can be modified with `tutor config save --set
PARAM_NAME=VALUE` commands.

Currently, you'll need to allow anonymous GET access to profile
images. Assuming a properly configured s3cmd, first create the
`S3_PROFILE_IMAGE_BUCKET` with public ACL set:

    s3cmd mb s3://openedx --acl-public

Next, set the policy for new objects. Create a `policy.json` file,
substituting `openedx` for the configured value of
`S3_PROFILE_IMAGE_BUCKET`, and `www.example.com` for the LMS domain::

    {
      "Version": "2012-10-17",
      "Statement": [{
        "Sid":"AddPerm",
        "Effect":"Allow",
        "Principal": "*",
        "Action": ["s3:GetObject"],
        "Resource": ["arn:aws:s3:::openedx/*"],
        "Condition": {"StringEquals":{"aws:Referer":["www.example.com"]}
      }]
    }

Next, run:

    s3cmd setpolicy policy.json s3://openedx

*This requirement will be removed before the first proper release of
this plugin, and it will then use presigned URLs instead. If after
that transition you continue to use the same S3 bucket, you will need
to update your bucket and object ACLs.*
