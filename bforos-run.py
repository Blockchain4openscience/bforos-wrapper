#!/usr/local/bin/python3
import argparse
from subprocess import check_output, call

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
    call_metadata = dict(app_name=app_name,
                         app_version=app_version,
                         app_id=app_id,
                         app_args=args.app_args)
    print(call_metadata)
    call([args.open_science_app, *args.app_args])
    return


if __name__ == "__main__":
    bforos_run()
