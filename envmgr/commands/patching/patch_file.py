# Copyright (c) Trainline Limited, 2017. All rights reserved. See LICENSE.txt in the project root for license information.

import json
import os.path

from codecs import open
from hashlib import sha1
from appdirs import user_data_dir

class PatchFile(object):

    @staticmethod
    def get_filepath(cluster, env):
        app_dir = user_data_dir('envmgr', 'trainline')
        filename = 'patch_{0}_{1}'.format(cluster.lower(), env.lower())
        filename = '{0}.json'.format(sha1(filename).hexdigest())
        return os.path.join(app_dir, filename)

    @staticmethod
    def get_contents(cluster, env):
        patch_file = PatchFile.get_filepath(cluster, env)
        if os.path.exists(patch_file):
            with open(patch_file, encoding='utf-8') as file_data:
                return json.load(file_data)
        else:
            return None

    @staticmethod
    def write_content(cluster, env, content):
        patch_file = PatchFile.get_filepath(cluster, env)
        with open(patch_file, 'w', encoding='utf-8') as f:
            f.write(unicode(json.dumps(content, ensure_ascii=False)))
    
    @staticmethod
    def delete(cluster, env):
        os.remove(PatchFile.get_filepath(cluster, env))