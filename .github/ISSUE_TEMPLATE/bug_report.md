---
name: Bug report
about: Report a bug in tutor-contrib-s3
title: ''
labels: ''
assignees: ''

---

# Summary

Replace this with a short summary (one sentence or short paragraph) of
the issue you are seeing.

## What I did

Explain the steps you undertook that led to the unexpected behavior
you are observing. Please include relevant documentation snippets,
such as the `S3_*` settings from Tutor’s `config.yml`. It’s OK to
remove or mask credentials (like your `OPENEDX_AWS_*` settings), but
otherwise try to err on the side of sharing more rather than less
information.

## What I expected to happen

Explain how you expected Tutor to behave with your configuration.

## What actually happened

Explain how Tutor behaved differently than you expected.

## My environment

Please add some information about the environment that you’re working
in. At a minimum, include these items:

* Tutor version: (Insert the Tutor version you are using.)
* `tutor-contrib-s3` version: (Insert the plugin version you are
  using. If you installed from Git, enter the tag or branch name, or
  the commit reference)

Additionally, you might also want to add any of the items below, if
you think they might be relevant to the bug:

* Kubernetes versions: (If you are reporting a bug that
  applies to deploying this plugin with `tutor k8s`, add your `kubectl
  version` output. Otherwise, remove this item.)
* Docker/Podman version: (If you are running `tutor local`, the output
  of `docker version` might be relevant.)
* Platform details: (Some issues are specific to individual cloud
  platforms. It may help if you could include whether you’re running
  on AWS, on OpenStack, on Digital Ocean etc.)
* S3 implementation details: (Some issues are specific to AWS S3,
  others to Ceph Object Gateway, others to other S3 implementations.
  It may help if you could include some details about what runs your
  S3 API.)

**Additional context**

If there’s any other context you’d like to share, please add it
here. Otherwise, you can delete this section.
