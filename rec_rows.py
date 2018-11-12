import requests
import json
import time
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--token", help="dss session token", type=str, default="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjb250ZXh0Ijp7InByb2ZpbGVzIjpbeyJhY3RpdmUiOnRydWUsInR5cGUiOiJ1cm46YmFtdGVjaDpwcm9maWxlIiwiaWQiOiJ1c2VyXzEiLCJwYXJlbnRhbF9jb250cm9scyI6eyJlbmFibGVkIjpmYWxzZX19XX19.D-oSieYZYy58YZBMv_lSm_i0-LR1zqSCNK3r1XRl7V8")
parser.add_argument("--url", help="url", type=str, default="http://watch.product.api.qa.espn.com/api/product/v3/watchespn/roku/featured?entitlements=ESPN_PLUS&appVersion=2.3&authStates=mvpd_previous&lang=en&deviceType=settop&favoriteSport=&favoriteTeam=&zipcode=94850&countryCode=US&tz=-8&iapPackages=ESPN_PLUS")
args = parser.parse_args()

print '==========='

s = requests.Session()
s.headers.update({'dss-session-token': args.token})
resp_json = s.get(args.url).json()

rec_buckets = int(0)
for bucket in resp_json['page']['buckets']:
    if bucket['name'] == 'Recommended for You':
        for content in bucket['contents']:
            print content['name']
            print content['streams'][0]['dss']
        rec_buckets += 1

if rec_buckets == 0:
    print 'No Recommended for You row found'

filename = 'output/output_dss_token_%s.json' % time.strftime('%Y%m%d_%H%M_%S')
text_file = open(filename, "w")
text_file.write(json.dumps(resp_json, indent=2))
text_file.close()

print '==========='
print 'output saved to %s' % filename