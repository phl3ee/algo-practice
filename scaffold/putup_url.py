"""Scrape a leetcode URL for details and feed it into putup_algo
"""
import requests
import argparse

#We can consume the leetcode URL and populate the params (and examples)
#   https://leetcode.com/problems/remove-duplicates-from-sorted-array/
parser = argparse.ArgumentParser(description='Pull leetcode problem from URL and invoke scaffolding')
parser.add_argument("-u", "--url", type=str, help='URL of the problem')
parser.add_argument("-t", "--timeout", type=float, default=1.0, help='Timeout on request, default 1.0 sec')

args = parser.parse_args()
url = args.url.strip()
timeoutSecs = args.timeout

r = requests.get(url, timeout=timeoutSecs)

#Shelving this for the moment as webpage content is complex
print(r)