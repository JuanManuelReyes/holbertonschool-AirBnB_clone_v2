#!/usr/bin/python3
"""
Write a Fabric script (based on the file 1-pack_web_static.py) that
distributes an archive to your web servers, using the function do_deploy
"""

from fabric.api import run, put, env
from os.path import exists

env.hosts = ['54.226.217.39', '34.229.176.58']


def do_deploy(archive_path):
        """Comment"""

        if not os.pathexists(archive_path):
                return False
        else:
                try:
                        put(archive_path, '/tmp/')

                        file_name = archive_path.split('/')
                        file_without_extension = file_name[1].split('.')
                        file = "/data/web_static/releases/" + file_without_extension[0] + "/"

                        run("mkdir -p" + " " + file)
                        run("tar -xzf /tmp/" + file_name[1] + " -C" + file)
                        run("rm /tmp/" + file_name[1])
                        run("mv " + file + "web_static/*" + " " + "/" + file_name)
                        run("rm -rf " + file + "web_static")
                        run("rm -rf /data/web_static/current")
                        run("ln -s " + file + " " + "/data/web_static/current")
                        return True
                except:
                        return False
