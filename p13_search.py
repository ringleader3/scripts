#!/usr/local/bin/python
import requests
import json_helper
import argparse
import json
import os

parser = argparse.ArgumentParser()
parser.add_argument("--token", help="dss session token", type=str, default="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjb250ZXh0Ijp7InByb2ZpbGVzIjpbeyJhY3RpdmUiOnRydWUsInR5cGUiOiJ1cm46YmFtdGVjaDpwcm9maWxlIiwiaWQiOiJ1c2VyXzEiLCJwYXJlbnRhbF9jb250cm9scyI6eyJlbmFibGVkIjpmYWxzZX19XX19.D-oSieYZYy58YZBMv_lSm_i0-LR1zqSCNK3r1XRl7V8")
parser.add_argument("--swid", help="swid", type=str, default="605C124C-EB99-40FC-9643-32D571A911DE")
parser.add_argument("--url", help="url", type=str, default="https://search-api-qa.svcs.plus.espn.com/svc/search/v2/graphql/persisted/query/espn/ExperimentSet")
args = parser.parse_args()

print '==========='
resp_json = json_helper.request_json(args.url, {'Authorization': 'Bearer %s' % args.token})

pretty_json = json.dumps(resp_json, indent=2)
print pretty_json

json_helper.output_file(os.path.basename(__file__), resp_json)

exit()