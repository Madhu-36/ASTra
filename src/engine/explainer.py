from typing import Optional

class EvidenceEngine:
    """
    Explanation Engine linking execution traces back to original AST slices.
    """
    
    @staticmethod
    def generate_explanation(action: str, success: bool, output: str, ast_context: Optional[str] = None) -> str:
        """
        Formats the execution results with the motivating AST context for the user.
        """
        status_str = "SUCCESS" if success else "FAILED/BLOCKED"
        
        explanation = f"### Action Execution Report\n"
        explanation += f"**Action**: `{action}`\n"
        explanation += f"**Status**: {status_str}\n\n"
        
        if ast_context:
            explanation += f"**Relevant Source Context (AST Slice)**:\n```python\n{ast_context.strip()}\n```\n\n"
            
        explanation += f"**System Output/Evidence**:\n```\n{output.strip()}\n```\n"
        
        return explanation
