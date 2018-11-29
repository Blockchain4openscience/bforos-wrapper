#!/usr/local/bin/python3
import argparse
from subprocess import check_output, call
import json
import urllib.request
import ssl


parser = argparse.ArgumentParser(description='Track usage of an Open Science App using BFOROS.')
parser.add_argument('open_science_app', metavar='<command>', type=str, help='Command to track')
parser.add_argument('app_args', metavar='<arguments>', type=str, nargs='*', help='Command to track')


def bforos_run():
    args = parser.parse_args()
    os_app_info = check_output([args.open_science_app, "-v"]).decode("utf-8").strip()
    header = os_app_info.split('\n')[0]
    app_name = header.split('v')[0].strip()
    app_version = header.split('v')[1].strip()
    app_id = os_app_info.split('\n')[1].replace('BFOROS Id: ', '').strip()

    bforos_data = {
        "$class": "org.bforos.CountRO",
        "researchObj": "resource:org.bforos.ResearchOJ#{}".format(app_id),
        "description": """
        APP NAME: {},
        APP VERSION: {},
        APP ARGS: {}
        """.format(app_name, app_version, args)
    }
    bforos_register_usage(bforos_data)
    call([args.open_science_app, *args.app_args])
    return


def bforos_register_usage(request_body):
    ssl._create_default_https_context = ssl._create_unverified_context
    bforos_url = 'https://labs.linkingdata.io:3000/api/CountRO'
    req = urllib.request.Request(bforos_url)
    req.add_header('Content-Type', 'application/json; charset=utf-8')
    json_data = json.dumps(request_body)
    json_data = json_data.encode('utf-8')
    req.add_header('Content-Length', len(json_data))
    response = urllib.request.urlopen(req, json_data)
    return response


if __name__ == "__main__":
    bforos_run()
