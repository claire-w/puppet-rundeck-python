#!/usr/bin/env python3
#coding: utf8
#  vim: set sw=4

import yaml
import argparse
import os, sys, time
from itertools import islice
from datetime import datetime, timedelta
import glob
from code.helper import *



def cut_line_1(fin,tmp_file):
    with open(fin, 'r') as f0:
        data = f0.read().splitlines(True)
    with open(tmp_file, 'w') as fout:
        fout.writelines(data[1:])

def generate_yaml(path, filehandle, node):
    tmp_file = '/tmp/tmpfile.yaml'

    logv("working on file: %s" % path)

    if not os.path.isfile(path):
        print('file does not exist: %s' % path)
        sys.exit(1)
    else:
        cut_line_1(path,tmp_file)
        f = open(tmp_file, 'r')
        yaml_data = yaml.load(f)

        tags = yaml_data['parameters']['datacenter'] + ',' + yaml_data['parameters']['node_environment'] + ',' + yaml_data['parameters']['node_type'] + ',' + yaml_data['parameters']['os']['lsb']['distcodename'] + ',' + yaml_data['parameters']['node_envid']
        d = {yaml_data['parameters']['hostname']:{'hostname':yaml_data['name'], 'osFamily':yaml_data['parameters']['osfamily'], 'osVersion':yaml_data['parameters']['os']['release']['full'], 'osName':yaml_data['parameters']['os']['lsb']['distdescription'], 'osArch':yaml_data['parameters']['architecture'], 'tags':tags}}
        f.close()

        yaml.dump(d, filehandle, default_flow_style=False)
