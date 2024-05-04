#!/usr/bin/python3
"""
Based on 1-pack_web_static.py, this fabric script
distributes archives to web servers.
"""

import os
from fabric.api import env, put, run

env.hosts = ['142.44.167.228', '144.217.246.195']


def do_deploy(archive_path):
    """distributes an archive to the web servers"""
    if not os.path.exists(archive_path):
        return False

    try:
        file_name = os.path.basename(archive_path)
        base_name = os.path.splitext(file_name)[0]
        target_path = "/data/web_static/releases/"

        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(target_path, base_name))
        run('tar -xzf /tmp/{} -C {}{}/'
            .format(file_name, target_path, base_name))
        run('rm /tmp/{}'.format(file_name))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(target_path, base_name))
        run('rm -rf {}{}/web_static'.format(target_path, base_name))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'
            .format(target_path, base_name))
        return True
    except Exception:
        return False
