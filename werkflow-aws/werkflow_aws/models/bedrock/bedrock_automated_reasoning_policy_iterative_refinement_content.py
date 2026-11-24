from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .bedrock_automated_reasoning_policy_build_workflow_document import BedrockAutomatedReasoningPolicyBuildWorkflowDocument


class BedrockAutomatedReasoningPolicyIterativeRefinementContent(BaseModel):
    documents: list[BedrockAutomatedReasoningPolicyBuildWorkflowDocument]
    feedback: StrictStr | None = None
