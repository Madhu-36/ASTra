# System Architecture: Security-First, Repository-Local Action Layer

Here is the architectural design for the prototype, detailing the flow from user intent to execution and explanation.

```mermaid
graph TD
    User([Developer / CI Webhook]) -->|Natural Language Intent & Diffs| CLI[CLI / API Endpoint]
    
    subgraph "1. Method-Level Slicer & Parser"
        CLI --> Parser[Tree-sitter AST Parser]
        Parser --> Slicer[Code Slicer]
        Slicer -->|Method-level Context| RAG
    end

    subgraph "2. Local Repository RAG"
        RAG[(Local RAG Store)] 
        RAG -->|Vector/Graph Index (ChromaDB/DuckDB)| Retriever[Context Retriever]
        Retriever -->|Enriched Context| Policy
    end

    subgraph "3. Intent Classifier & Policy Gate"
        Policy[Risk Policy Engine]
        Policy --> Classifier[LLM Intent Classifier]
        Classifier --> Tier1{Tier 1: Read-Only}
        Classifier --> Tier2{Tier 2: Sandbox Write}
        Classifier --> Tier3{Tier 3: Destructive}
    end

    subgraph "4. Execution Harness"
        Tier1 -->|Auto Execute| Executor[Sandbox Executor]
        Tier2 -->|Isolated Patch/Test| Executor
        Tier3 -->|Prompt User| HumanGate[Human Confirmation]
        HumanGate -->|Approve| Executor
        HumanGate -->|Reject| Abort[Abort Action]
        
        Executor -->|Stdout/Stderr/Coverage| Validator[Feedback Loop]
        Validator -->|Refine if Failed| Classifier
    end

    subgraph "5. Explanation Engine"
        Validator -->|Success/Results| Explainer[Evidence Engine]
        Explainer -->|Grounded Explanation| User
        Abort --> Explainer
    end

    %% Styling
    classDef safe fill:#e1f5fe,stroke:#03a9f4,stroke-width:2px;
    classDef warning fill:#fff3e0,stroke:#ff9800,stroke-width:2px;
    classDef danger fill:#ffebee,stroke:#f44336,stroke-width:2px;
    
    class Tier1 safe;
    class Tier2 warning;
    class Tier3 danger;
```

### Component Breakdown
1. **Slicer (`src/slicer`)**: Uses `tree-sitter` to parse code into ASTs. When given a diff, it extracts only the surrounding method/class, minimizing the context window and avoiding the hallucination-prone whole-file approach.
2. **Retrieval (`src/retrieval`)**: Embeds method slices and project documentation locally. Retrieves strictly relevant context to ground the LLM's understanding.
3. **Policy Gate (`src/policy`)**: Classifies the generated command/action. Tier 1 (Safe) executes automatically. Tier 2 executes in a sandbox for testing. Tier 3 (Destructive like `git push` or `rm`) blocks execution pending explicit approval.
4. **Sandbox (`src/sandbox`)**: A lightweight container or subprocess wrapper that safely captures outputs and traces for the iterative feedback loop.
5. **Engine (`src/engine`)**: Links the execution trace back to the original AST slice to provide the user with clear, evidence-backed explanations.
