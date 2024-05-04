#!/usr/bin/python3
"""
This script, a modified version of 2-do_deploy_web_static.py,
 includes archive building and delivery to web servers.
"""

from fabric.api import run, put, local, env
from datetime import datetime
from os.path import isdir, exists

# Define the server hosts
env.hosts = ['142.44.167.228', '144.217.246.195']


def do_pack():
    """From web_static, create a.tgz archive."""
    try:
        current_time = datetime.now().strftime("%Y%m%d%H%M%S")
        target_dir = "versions"
        if not isdir(target_dir):
            local(f"mkdir {target_dir}")
        archive_name = f"{target_dir}/web_static_{current_time}.tgz"
        local(f"tar -cvzf {archive_name} web_static")
        return archive_name
    except Exception:
        return None


def do_deploy(archive_path):
    """Deploy the archive to the web servers."""
    if not exists(archive_path):
        return False
    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        release_path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run(f"mkdir -p {release_path}{base_name}/")
        run(f"tar -xzf /tmp/{file_name} -C {release_path}{base_name}/")
        run(f"rm /tmp/{file_name}")
        run(f"mv {release_path}{base_name}/web_static/* "
            f"{release_path}{base_name}/")
        run(f"rm -rf {release_path}{base_name}/web_static")
        run("rm -rf /data/web_static/current")
        run(f"ln -s {release_path}{base_name}/ /data/web_static/current")
        return True
    except Exception:
        return False


def deploy():
    """Use pack and deploy to distribute a new archive."""
    path_to_archive = do_pack()
    if path_to_archive is None:
        return False
    return do_deploy(path_to_archive)
