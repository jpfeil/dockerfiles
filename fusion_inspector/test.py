#!/usr/bin/env python2.7
# John Vivian
import subprocess
import tempfile
import unittest


class TestFusionInspector(unittest.TestCase):

    def test_docker_call(self):
        out, err = check_docker_output(tool='jpfeil/fusion_inspector')

def check_docker_output(tool):
    command = 'docker run ' + tool
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = process.communicate()
    return output

if __name__ == '__main__':
    unittest.main()
