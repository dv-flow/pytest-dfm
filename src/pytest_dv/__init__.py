import os
import pytest

@pytest.fixture
def dvflow(request, tmpdir):
    from .dv_flow import DvFlow
    return DvFlow(request, os.path.dirname(request.fspath), tmpdir)
