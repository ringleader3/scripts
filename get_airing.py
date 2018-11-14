import json_helper
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--airing", help="airing", type=str, default="3432424")
args = parser.parse_args()

print json_helper.get_airing_from_airing_id(args.airing)