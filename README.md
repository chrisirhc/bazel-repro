# Reproduction

On a Linux machine:
```sh
 % bazel build ...
INFO: Analyzed 4 targets (0 packages loaded, 8 targets configured).
ERROR: …/bazel-repro/BUILD.bazel:11:21: mypy //:helloworld_python_proto failed: (Exit 2): mypy failed: error executing mypy command (from target //:helloworld_python_proto) bazel-out/darwin_arm64-opt-exec-ST-47de9cc097ad/bin/external/rules_mypy+/mypy/private/mypy --output bazel-out/darwin_arm64-fastbuild/bin/helloworld_python_proto.mypy_stdout --cache-dir ... (remaining 5 arguments skipped)

Use --sandbox_debug to see verbose messages from the sandbox and retain the sandbox build root for debugging
bazel-out/darwin_arm64-fastbuild/bin/helloworld_python_proto_pb/helloworld_pb2.pyi: error: Duplicate module named "helloworld_pb2" (also at "bazel-out/darwin_arm64-fastbuild/bin/helloworld_python_proto_pb/helloworld_pb2.py")
bazel-out/darwin_arm64-fastbuild/bin/helloworld_python_proto_pb/helloworld_pb2.pyi: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#mapping-file-paths-to-modules for more info
bazel-out/darwin_arm64-fastbuild/bin/helloworld_python_proto_pb/helloworld_pb2.pyi: note: Common resolutions include: a) using `--exclude` to avoid checking one of them, b) adding `__init__.py` somewhere, c) using `--explicit-package-bases` or adjusting MYPYPATH
```

If `generate_pyi` is removed from `helloworld_python_proto`, then the build fails in another way:
```
 % bazel build //...                                  
INFO: Analyzed 4 targets (0 packages loaded, 7 targets configured).
ERROR: …/bazel-repro/BUILD.bazel:18:10: mypy //:helloworld_example failed: (Exit 1): mypy failed: error executing mypy command (from target //:helloworld_example) bazel-out/darwin_arm64-opt-exec-ST-47de9cc097ad/bin/external/rules_mypy+/mypy/private/mypy --output bazel-out/darwin_arm64-fastbuild/bin/helloworld_example.mypy_stdout --cache-dir ... (remaining 6 arguments skipped)

Use --sandbox_debug to see verbose messages from the sandbox and retain the sandbox build root for debugging
helloworld_example.py:15: error: Module has no attribute "HelloRequest"  [attr-defined]
helloworld_example.py:21: error: Module has no attribute "HelloReply"  [attr-defined]
Found 2 errors in 1 file (checked 1 source file)
INFO: Elapsed time: 2.774s, Critical Path: 2.49s
INFO: 6 processes: 620 action cache hit, 5 internal, 1 darwin-sandbox.
ERROR: Build did NOT complete successfully,
```