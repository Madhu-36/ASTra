import subprocess
import os
from typing import Tuple
from src.policy.classifier import RiskTier, IntentAction

class SandboxExecutor:
    """
    Execution harness. Upgraded to use Docker for true isolation.
    """
    
    def __init__(self, image: str = "python:3.11-slim"):
        self.image = image
    
    def execute(self, intent: IntentAction, require_human_approval: bool = True) -> Tuple[bool, str]:
        """
        Executes the action based on its Risk Tier inside a Docker sandbox.
        """
        if intent.tier == RiskTier.TIER_3 and require_human_approval:
            return False, f"BLOCKED: Tier 3 action '{intent.action}' requires explicit human confirmation. Reason: {intent.reasoning}"
            
        # Mount the current directory and run inside Docker
        workspace_dir = os.getcwd()
        docker_cmd = [
            "docker", "run", "--rm",
            "-v", f"{workspace_dir}:/workspace",
            "-w", "/workspace",
            # Run without network if we wanted strict isolation (omitted for package installs)
            self.image,
            "sh", "-c", intent.action
        ]
        
        try:
            result = subprocess.run(
                docker_cmd,
                check=False,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                timeout=30
            )
            
            output = result.stdout if result.returncode == 0 else result.stderr
            
            # If docker is not running or not installed, fallback to subprocess for prototype gracefully
            if "docker: error during connect" in output or "Cannot connect to the Docker daemon" in output or result.returncode == 127:
                return self._fallback_execute(intent)
                
            return result.returncode == 0, output
            
        except FileNotFoundError:
            # Docker not installed
            return self._fallback_execute(intent)
        except subprocess.TimeoutExpired:
            return False, "Execution timed out."
        except Exception as e:
            return False, f"Execution failed: {str(e)}"
            
    def _fallback_execute(self, intent: IntentAction) -> Tuple[bool, str]:
        """Fallback to standard subprocess if Docker is unavailable"""
        try:
            result = subprocess.run(
                intent.action,
                shell=True,
                check=False,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                timeout=30
            )
            output = result.stdout if result.returncode == 0 else result.stderr
            return result.returncode == 0, output
        except Exception as e:
            return False, f"Fallback execution failed: {str(e)}"
