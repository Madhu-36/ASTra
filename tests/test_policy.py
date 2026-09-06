import pytest
from src.policy.classifier import PolicyGate, RiskTier
from src.sandbox.executor import SandboxExecutor

def test_tier1_safe_action():
    intent = PolicyGate.classify_action("echo hello")
    assert intent.tier == RiskTier.TIER_1
    
    executor = SandboxExecutor()
    # Should execute without blocking
    success, _ = executor.execute(intent, require_human_approval=True)
    assert success is True

def test_tier3_destructive_action_is_blocked():
    intent = PolicyGate.classify_action("rm -rf /")
    assert intent.tier == RiskTier.TIER_3
    
    executor = SandboxExecutor()
    success, output = executor.execute(intent, require_human_approval=True)
    
    # Action must be intercepted and blocked
    assert success is False
    assert "BLOCKED: Tier 3 action" in output
    assert "rm" in output

def test_tier3_destructive_action_with_approval():
    intent = PolicyGate.classify_action("git push origin main")
    assert intent.tier == RiskTier.TIER_3
    
    executor = SandboxExecutor()
    # Simulating human approval by setting require_human_approval=False
    # (Since git push might fail in dummy env, we just check it doesn't return the BLOCKED msg)
    success, output = executor.execute(intent, require_human_approval=False)
    
    assert "BLOCKED" not in output
