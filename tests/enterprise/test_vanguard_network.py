import pytest
from src.enterprise.vanguard_network.service import VanguardNetworkService
def test_vanguard_network_service():
    assert VanguardNetworkService().execute() == 'enterprise_ready'
