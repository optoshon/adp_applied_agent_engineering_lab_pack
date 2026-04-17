# Applied Agent Engineering Lab Pack — SageMaker Expanded Version

This is the expanded classroom-ready pack rebuilt for your current delivery constraints:

- SageMaker notebook friendly
- AWS / Bedrock oriented
- Azure removed from the new add-on notebooks
- S3 used as input only
- local notebook storage or pandas DataFrames used for run metadata
- learner mini-hacks included in each added notebook

## What was added

### M1
- `M1B_LoRA_QLoRA_Quantization_SageMaker.ipynb`
  - built from your uploaded LoRA/QLoRA notebook
  - classroom-safe adapter fine-tuning flow
  - LoRA + optional QLoRA path
  - local artifacts only

### M2
- `M2B_Observable_RAG_Evaluation_SageMaker.ipynb`
  - built from your stepwise observable RAG script
  - retrieval traces, prompt capture, evaluation tables

- `M2C_Semantic_Chunking_RBAC_RAG_SageMaker.ipynb`
  - built from your semantic chunking + RBAC script
  - secure retrieval pattern for enterprise HR-style questions

### M4
- `M4B_Strands_Agents_SageMaker.ipynb`
  - new Strands-based classroom notebook
  - uses Bedrock + Strands tools
  - keeps workflow state in pandas DataFrames
  - avoids backend JSON persistence

## Important note on the uploaded multimodal scripts

Your uploaded multimodal Docling / table / text / image / ensemble files are useful, but in their current form they are tightly coupled to:
- Azure OpenAI environment variables
- hardcoded Windows paths
- file-based manifests / JSON sidecars

I preserved them as reference inputs for the next conversion pass. The current expanded pack focuses first on the fastest classroom-safe SageMaker conversion for learners.

## Suggested teaching order now

1. `M1_LLM_Foundations_Classroom_Ready.ipynb`
2. `M1B_LoRA_QLoRA_Quantization_SageMaker.ipynb`
3. `M2_RAG_Fundamentals_Classroom_Ready.ipynb`
4. `M2B_Observable_RAG_Evaluation_SageMaker.ipynb`
5. `M2C_Semantic_Chunking_RBAC_RAG_SageMaker.ipynb`
6. `M3_Governance_Evaluation_Traceability_Classroom_Ready.ipynb`
7. `M4B_Strands_Agents_SageMaker.ipynb`

## Suggested next pass after you upload more files
- convert the multimodal RAG set into one or two SageMaker notebooks
- refactor the current M4 notebook to use the same Strands + DataFrame pattern throughout
- add instructor-only solution notes and expected outputs for each learner mini-hack
