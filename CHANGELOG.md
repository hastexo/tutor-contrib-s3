## Unreleased

* [Enhancement] Use Tutor v1 plugin API.

## Version 0.2.2 (2022-05-05)

* [Enhancement] If `S3_PROFILE_IMAGE_BUCKET` is not set, store profile 
  images in the filesystem. This matches Tutor's default behavior (when 
  running without plugins). If a bucket name is provided, upload profile 
  images to S3.
* [Fix] Add a dummy `base_url` to profile image backend to prevent
  it from crashing LMS when running with `DEBUG=True` (such as when using
  `tutor dev`).

## Version 0.2.1 (2022-03-31)

* [Fix] Change the defaults for `S3_HOST`, `S3_PORT`, and
  `S3_PROFILE_IMAGE_CUSTOM_DOMAIN` from `None` to the empty
  string. Also, change the default for `S3_USE_SSL` from the string
  `"True"` to the boolean `True`.

## Version 0.2.0 (2022-03-01)

* [Enhancement] Add `S3_CUSTOM_DOMAIN` to set a custom domain for S3.
* [Enhancement] Add `S3_PROFILE_IMAGE_CUSTOM_DOMAIN` to set custom domain for 
  profile images.

## Version 0.1.2 (2022-02-22)
 
* [Fix] Rather than incorrectly relying on `ENABLE_HTTPS`, honour
  `S3_USE_SSL` when setting `AWS_S3_ENDPOINT_URL`.
* [Fix] Only populate the `AWS_S3_ENDPOINT_URL` Open edX setting if
  `S3_HOST` is set, and recommend leaving `S3_HOST` and `S3_PORT`
  unset if using AWS S3 (as opposed to an S3-compatible API).
* [Fix] Default for `S3_ADDRESSING_STYLE` is now `"auto"` to use 
  the same default as the ORA2 S3 backend, and the AWS S3 CLI.

## Version 0.1.1 (2022-01-13)

* [Fix] `S3_FILE_UPLOAD_BUCKET` parameter was ignored. Use it to set
  `FILE_UPLOAD_STORAGE_BUCKET_NAME`.

## Version 0.1.0 (2022-01-12)

* [Enhancement] Rename from tutor-s3 to tutor-contrib-s3 (this plugin
  is not affiliated with [the Tutor
  project](https://docs.tutor.overhang.io/)).
* [Enhancement] Support S3Boto3Storage, instead of the deprecated
  S3BotoStorage.
* [Enhancement] No longer rely on buckets with a public ACL, use
  query-string authentication instead.

## Version 0.0.1 (2019-10-10)

**Experimental. Do not use in production.**

* Initial Git import
