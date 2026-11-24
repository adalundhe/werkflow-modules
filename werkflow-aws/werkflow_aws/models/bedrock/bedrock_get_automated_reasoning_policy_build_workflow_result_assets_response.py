from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .bedrock_automated_reasoning_policy_build_result_assets import BedrockAutomatedReasoningPolicyBuildResultAssets


class BedrockGetAutomatedReasoningPolicyBuildWorkflowResultAssetsResponse(BaseModel):
    policyArn: StrictStr | None = None
    buildWorkflowId: StrictStr | None = None
    buildWorkflowAssets: BedrockAutomatedReasoningPolicyBuildResultAssets | None = None
    ResponseMetadata: dict[str, Any] | None = None
