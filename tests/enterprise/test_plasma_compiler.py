import pytest
from src.enterprise.plasma_compiler.service import PlasmaCompilerService
def test_plasma_compiler_service():
    assert PlasmaCompilerService().execute() == 'optimized'
