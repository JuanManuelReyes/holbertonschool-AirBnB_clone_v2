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
	if exists(archive_path) is False:
		return False
	try:
		file_no_extension = archive_path.split('.')[0]
		file_extension = archive_path.split('/')[1]
		input_path = "/data/web_static/releases/{}/".format(file_no_extension)
  
		put(archive_path, "/tmp/")
		run("sudo mkdir -p {}".format(input_path))
		run("sudo tar -zxvf /tmp/{} -C {}".format(file_extension, input_path))
		run("sudo rm -rf /tmp/{}".format(file_extension))
		run("sudo mv -n {}/web_static/* {}".format(input_path, input_path))
		run("sudo rm -rf {}/web_static".format(input_path))
		run("sudo rm /data/web_static/current")
		run("sudo ln -s {} /data/web_static/current".format(input_path))
		print("New version deployed!")
		return True
		
	except Exception:
		return False
