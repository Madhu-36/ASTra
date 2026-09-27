import pytest
from src.enterprise.aegis_auth.service import AegisAuthService
def test_aegis_auth_service():
    assert AegisAuthService().execute() == 'enterprise_ready'
