import pytest
from mbtest.server import MountebankServer


@pytest.fixture(scope="session")
def mock_server(request):
    return MountebankServer(port=2525, host="m")