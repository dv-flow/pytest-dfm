import pytest
from pytest_dfm import *

def test_smoke(dvflow):

    msg = dvflow.mkTask("std.Message", name="msg", msg="Hello World!")
    dvflow.runTask(msg)

    pass