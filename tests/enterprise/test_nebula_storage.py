import pytest
from src.enterprise.nebula_storage.service import NebulaStorageService
def test_nebula_storage_service():
    assert NebulaStorageService().execute() == 'optimized'
