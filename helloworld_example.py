"""Sample usage of the `helloworld.proto` definitions from Python.

This script constructs request and reply messages, demonstrates serialization,
and prints their contents.
"""

from __future__ import annotations

import base64

import helloworld_pb2


def main() -> None:
    request = helloworld_pb2.HelloRequest(name="Bazel")
    print(f"Request: name={request.name!r}")

    serialized_request = request.SerializeToString()
    print(f"Serialized (base64): {base64.b64encode(serialized_request).decode('ascii')}")

    reply = helloworld_pb2.HelloReply(message=f"Hello, {request.name}!")
    print(f"Reply: message={reply.message!r}")


if __name__ == "__main__":
    main()

