import pytest
from src.enterprise.aether_gateway.service import AetherGatewayService
def test_aether_gateway_service():
    assert AetherGatewayService().execute() == 'optimized'
