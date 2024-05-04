#!/usr/bin/python3
"""
Use the Fabric script to create a tgz archive from the web_static
folder in the AirBnB Clone repo.

"""

import os
from datetime import datetime
from fabric.operations import local


def do_pack():
    """generates a tgz archive"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if not os.path.isdir("versions"):
            local("mkdir versions")
        file_name = f"versions/web_static_{date}.tgz"
        local(f"tar -cvzf {file_name} web_static")
        return file_name
    except Exception:
        return None
