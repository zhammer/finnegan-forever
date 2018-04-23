#!/usr/bin/env python3

"""Script for creating a valid unicode scroll file."""

import argparse
import unicodedata


def _parse_args():
    """Helper function to create the command-line argument parser for create_unicode_scroll. Return
    the parsed arguments as a Namespace object if successful. Exits the program if unsuccessful or
    if the help message is printed.
    """
    description = ('Create a valid unicode scroll file for a finnegan_forever.gateways.unicode_scroll.')
    epilog = ('The scroll gateway provides an interface for reading passages of `passage_size`\n'
              'characters from a text document starting at a given character `offset`.\n'
              'This is easily implemented for ascii-encoded files, where each character is\n'
              'represented by one byte. Documents containing unicode characters, however, must be\n'
              'specially encoded so that each character is represented by a fixed `character_size`\n'
              'for O(1) character indexing. This can be done using utf32 encoding with a few tricks.\n'
              '1. Encode the input text as "utf-32-be" (utf 32 bigendian with no BOM).\n'
              '2. Normalize the bytes in the "NFC" form (this removes unnecessary combining characters).\n'
              '3. Remove any combining characters from the unicode data that could not be normalized.\n')

    parser = argparse.ArgumentParser(description=description,
                                     epilog=epilog,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument('-s', '--source-file',
                        required=True,
		        help='Source text file path.')

    parser.add_argument('-o', '--output-file',
                        required=True,
		        help='Output valid unicode scroll file path.')

    parser.add_argument('-n', '--squash-whitespace',
                        required=False,
                        action='store_true',
		        help='If true, squash all whitespace characters to one space character.')

    return parser.parse_args()


def squash_whitespace(text):
    """Squash all single or repeating whitespace characters in `text` to one space character.

    >>> squash_whitespace('my     name \t\t is  \\n  zach.')
    'my name is zach.'
    """
    words = text.split()
    return ' '.join(words)


def encode_scroll(text):
    """Encode text in the valid scroll file utf32 encoding. Returns encoded bytes."""
    text = unicodedata.normalize('NFC', text)
    text = ''.join((char for char in text if not unicodedata.combining(char)))
    return text.encode('utf-32-be')


def main():
    """Main"""
    args = _parse_args()

    with open(args.source_file) as source:
        text = source.read()

    if args.squash_whitespace:
        text = squash_whitespace(text)

    encoded_bytes = encode_scroll(text)

    with open(args.output_file, 'wb') as output_file:
        output_file.write(encoded_bytes)


if __name__ == '__main__':
    main()
