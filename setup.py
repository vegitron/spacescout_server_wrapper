#!/usr/bin/env python

from distutils.core import setup
import subprocess
import sys
import os

path = os.path.dirname(os.path.realpath(__file__))

submodule_path = os.path.join(path, "spotseeker_server")

subprocess.call(["git", "submodule", "init"], cwd=path)
subprocess.call(["git", "submodule", "update"], cwd=path)


setup(name='SpaceScout-Server-Wrapper',
      version='1.0',
)

subprocess.call(["pip", "install", "-r", "requirements.txt"], cwd=submodule_path)
