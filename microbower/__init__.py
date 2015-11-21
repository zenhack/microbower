
from subprocess import check_call
import urllib
import json
import os
import os.path
import logging

logger = logging.getLogger(__name__)


def load_json_file(location, filename):
    try:
        with open(os.path.join(location, filename)) as f:
            ret = json.load(f)
    except ValueError:
        logger.warning('%r is not valid JSON, ignoring.', filename)
        ret = {}
    except OSError as e:
        logger.warning('Failed to open %r: %r. Ignoring.', filename, e)
        ret = {}
    if not isinstance(ret, dict):
        logger.warning('%r does not contain a dictionary. Ignoring.', filename)
        ret = {}
    return ret


def load_bowerrc(location='.'):
    bowerrc = load_json_file(location, '.bowerrc')
    bowerrc['directory'] = bowerrc.get('directory',
                                       os.path.join(location,
                                                    'bower_components'))
    return bowerrc


def load_bower_json(location='.'):
    bower_json = load_json_file(location, 'bower.json')
    bower_json['dependencies'] = bower_json.get('dependencies', {})
    return bower_json


def install():
    bowerrc = load_bowerrc()
    bower_json = load_bower_json()

    if not os.path.isdir(bowerrc['directory']):
        os.makedirs(bowerrc['directory'])

    registry = 'https://bower.herokuapp.com'
    topdir = os.path.abspath(os.curdir)

    for pkg in bower_json['dependencies'].keys():
        req = urllib.urlopen('%s/packages/%s' % (registry, pkg))
        info = json.load(req)
        os.chdir(bowerrc['directory'])
        if not os.path.isdir(os.path.join(pkg, '.git')):
            check_call(['git', 'clone', info['url'], pkg])
        os.chdir(pkg)
        install()
        os.chdir(topdir)
