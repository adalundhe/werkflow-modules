from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .bedrock_automated_reasoning_policy_build_workflow_summary import BedrockAutomatedReasoningPolicyBuildWorkflowSummary


class BedrockListAutomatedReasoningPolicyBuildWorkflowsResponse(BaseModel):
    automatedReasoningPolicyBuildWorkflowSummaries: list[BedrockAutomatedReasoningPolicyBuildWorkflowSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
