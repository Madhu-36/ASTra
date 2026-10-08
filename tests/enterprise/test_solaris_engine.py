import pytest
from src.enterprise.solaris_engine.service import SolarisEngineService
def test_solaris_engine_service():
    assert SolarisEngineService().execute() == 'optimized'
