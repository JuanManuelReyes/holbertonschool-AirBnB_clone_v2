#!/usr/bin/python3
"""
Write a Fabric script (based on the file 1-pack_web_static.py) that
distributes an archive to your web servers, using the function do_deploy
"""

from fabric.api import run, put, env
from os.path import exists

env.hosts = ['54.226.217.39', '34.229.176.58']


def do_deploy(archive_path):
    '''function'''
    if not os.path.exists(archive_path):
        return False
    else:
        try:
            put(archive_path, '/tmp/')
            path_name = archive_path.split('/')[1]
            path_name_no_ext = path_name.split('.')[0]
            file_name = "/data/web_static/releases/" + path_name_no_ext + "/"
            run("mkdir -p" + " " + file_name)
            run("tar -xzf /tmp/" + path_name + " -C" + file_name)
            run("rm /tmp/" + path_name)
            run("mv " + file_name + "web_static/*" + " " + "/" + file_name)
            run("rm -rf " + file_name + "web_static")
            run("rm -rf /data/web_static/current")
            run("ln -s " + file_name + " " + "/data/web_static/current")
            return True
        except:
            return False
