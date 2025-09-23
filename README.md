# Reproduction

On a Linux machine:
```sh
 % bazel test ...
ERROR: Failed to parse downloader config: Unable to find downloader config file common_downloader.cfg
 % bazel test --config=linux ...
ERROR: Failed to parse downloader config: Unable to find downloader config file linux_downloader.cfg
 % bazel test --enable_platform_specific_config ...
ERROR: Failed to parse downloader config: Unable to find downloader config file linux_downloader.cfg
```

It seems that using `--enable_platform_specific_config` as an argument is not equivalent to using it as in `.bazelrc`.
