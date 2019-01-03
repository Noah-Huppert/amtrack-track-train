#!/usr/bin/env python3
import sys
import argparse
import base64
import urllib.parse
import codecs

def main() -> int:
    """ Entry point
    Returns: Exit code
    """
    # Parse arguments
    parser = argparse.ArgumentParser(description="Decodes Amtrak messages")
    parser.add_argument('file',
                        help="Name of file to decode")
    args = parser.parse_args()

    # URL decode
    encoded_body = None
    with open(args.file, 'r') as f:
        encoded_body = f.read()

    part_to_decode = encoded_body[0:len(encoded_body)-88]
    #decoded_part = base64.b64decode(part_to_decode)
    #bytes_part = codecs.decode(decoded_part, 'utf8')
    print(part_to_decode)

    #decoded_body = urllib.parse.unquote_plus(encoded_body)

    return 0


if __name__ == '__main__':
    sys.exit(main())
