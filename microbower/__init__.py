
from subprocess import check_call
import urllib
import json
import os
import os.path


def install():
    if not (os.path.isfile('.bowerrc') and os.path.isfile('bower.json')):
        return
    with open('.bowerrc') as f:
        bowerrc = json.load(f)
    with open('bower.json') as f:
        bower_json = json.load(f)

    if not os.path.isdir(bowerrc['directory']):
        os.makedirs(bowerrc['directory'])

    registry = 'https://bower.herokuapp.com'
    topdir = os.path.abspath(os.curdir)

    for pkg in bower_json['dependencies'].keys():
        req = urllib.urlopen('%s/packages/%s' % (registry, pkg))
        info = json.load(req)
        os.chdir(bowerrc['directory'])
        check_call(['git', 'clone', info['url']])
        os.chdir(pkg)
        install()
        os.chdir(topdir)
