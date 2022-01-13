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
