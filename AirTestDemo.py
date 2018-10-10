# -*- encoding=utf8 -*-
__author__ = "tianle"

from airtest.core.api import *
from airtest.cli.runner import AirtestCase, run_script
from airtest.cli.parser import runner_parser


class AirTestDemo(AirtestCase):
    def setUp(self):
        print("custom setup")
        super(AirTestDemo, self).setUp()

    def tearDown(self):
        print("custom tearDown")
        super(AirTestDemo, self).setUp()


if __name__ == '__main__':
    ap = runner_parser()
    args = ap.parse_args()
    run_script(args, AirTestDemo)
