import tree_sitter_python as tspython
from tree_sitter import Language, Parser

class CodeSlicer:
    """
    Method-level code slicing using Tree-sitter.
    Extracts only the surrounding method/class for a given line,
    avoiding full-file context bloat.
    """
    def __init__(self):
        # In tree-sitter>=0.21.0, Language takes the language function directly
        self.PY_LANGUAGE = Language(tspython.language())
        self.parser = Parser(self.PY_LANGUAGE)

    def get_slice_for_line(self, source_code: str, line_number: int) -> str:
        """
        Extracts the function or class containing the given line number (1-indexed).
        """
        tree = self.parser.parse(bytes(source_code, "utf8"))
        root_node = tree.root_node

        # Find the node that contains the line
        target_node = self._find_node_at_line(root_node, line_number - 1)
        
        if not target_node:
            return ""

        # Walk up the tree to find the enclosing function or class
        parent = target_node
        while parent:
            if parent.type in ["function_definition", "class_definition"]:
                return source_code.encode("utf8")[parent.start_byte:parent.end_byte].decode("utf8")
            parent = parent.parent
            
        # Fallback to the line itself if no enclosing function/class found
        lines = source_code.splitlines()
        if 0 <= line_number - 1 < len(lines):
            return lines[line_number - 1]
        return ""

    def _find_node_at_line(self, node, line_index: int):
        # Check if this node spans the line
        if node.start_point[0] <= line_index <= node.end_point[0]:
            # Recurse to find the most specific child
            for child in node.children:
                result = self._find_node_at_line(child, line_index)
                if result:
                    return result
            return node
        return None
