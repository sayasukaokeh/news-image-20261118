#!/usr/bin/env python3
"""News-image entry for make.fun competition news-image-20261118.

Copies the bundled front-page image (assets/entry.png) to the output
directory as entry.png. The copy is byte-for-byte and deterministic: no
network, no timestamps, no randomness, so repeated runs write identical
bytes. Only the Python standard library is used.
"""

import os
import struct

MAX_BYTES = 1_048_576
MAX_DIMENSION = 1024
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def png_dimensions(data):
    """Return (width, height) from a PNG's IHDR chunk.

    Also rejects a truncated file: a whole PNG ends with the IEND chunk.
    """
    if len(data) < 33 or data[:8] != PNG_MAGIC:
        raise ValueError("not a PNG file")
    if data[12:16] != b"IHDR":
        raise ValueError("missing IHDR chunk")
    if data[-12:-8] != b"\x00\x00\x00\x00" or data[-8:-4] != b"IEND":
        raise ValueError("missing IEND chunk")
    width, height = struct.unpack(">II", data[16:24])
    return width, height


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "assets", "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    target = os.path.join(out_dir, "entry.png")

    with open(source, "rb") as handle:
        data = handle.read()

    width, height = png_dimensions(data)
    if width > MAX_DIMENSION or height > MAX_DIMENSION:
        raise ValueError(f"image is {width}x{height}, over the 1024 limit")
    if len(data) > MAX_BYTES:
        raise ValueError(f"image is {len(data)} bytes, over the 1 MiB limit")

    os.makedirs(out_dir, exist_ok=True)
    with open(target, "wb") as handle:
        handle.write(data)

    print(f"wrote {target} ({width}x{height}, {len(data)} bytes)")


if __name__ == "__main__":
    main()
