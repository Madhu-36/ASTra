import pytest
from src.enterprise.oracle_engine.service import OracleEngineService
def test_oracle_engine_service():
    assert OracleEngineService().execute() == 'optimized'
