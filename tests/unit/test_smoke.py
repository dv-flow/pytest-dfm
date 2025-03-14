import pytest
from pytest_dv import *

def test_smoke(dvflow):

    msg = dvflow.mkTask("std.Message", name="msg", msg="Hello World!")
    dvflow.runTask(msg)

    pass