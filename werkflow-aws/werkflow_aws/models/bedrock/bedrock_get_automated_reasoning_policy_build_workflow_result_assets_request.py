from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class BedrockGetAutomatedReasoningPolicyBuildWorkflowResultAssetsRequest(BaseModel):
    policyArn: StrictStr
    buildWorkflowId: StrictStr
    assetType: Literal['BUILD_LOG', 'QUALITY_REPORT', 'POLICY_DEFINITION', 'GENERATED_TEST_CASES', 'POLICY_SCENARIOS', 'FIDELITY_REPORT', 'ASSET_MANIFEST', 'SOURCE_DOCUMENT']
    assetId: StrictStr | None = None
