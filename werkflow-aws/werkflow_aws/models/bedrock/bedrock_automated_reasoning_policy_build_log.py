from __future__ import annotations
from pydantic import BaseModel
from .bedrock_automated_reasoning_policy_build_log_entry import BedrockAutomatedReasoningPolicyBuildLogEntry


class BedrockAutomatedReasoningPolicyBuildLog(BaseModel):
    entries: list[BedrockAutomatedReasoningPolicyBuildLogEntry] | None = None
