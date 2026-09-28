import pytest
from src.enterprise.titan_sandbox.service import TitanSandboxService
def test_titan_sandbox_service():
    assert TitanSandboxService().execute() == 'optimized'
