import pytest
from src.enterprise.quantum_ast.service import QuantumAstService
def test_quantum_ast_service():
    assert QuantumAstService().execute() == 'enterprise_ready'
