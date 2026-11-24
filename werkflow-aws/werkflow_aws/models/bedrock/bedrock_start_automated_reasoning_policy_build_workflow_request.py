from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .bedrock_automated_reasoning_policy_build_workflow_source import BedrockAutomatedReasoningPolicyBuildWorkflowSource


class BedrockStartAutomatedReasoningPolicyBuildWorkflowRequest(BaseModel):
    policyArn: StrictStr
    buildWorkflowType: Literal['INGEST_CONTENT', 'REFINE_POLICY', 'IMPORT_POLICY', 'GENERATE_FIDELITY_REPORT', 'GENERATE_POLICY_SCENARIOS', 'RESOLVE_POLICY_AMBIGUITIES', 'ITERATIVELY_REFINE_POLICY']
    sourceContent: BedrockAutomatedReasoningPolicyBuildWorkflowSource
    clientRequestToken: StrictStr | None = None
