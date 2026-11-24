from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockAutomatedReasoningPolicyBuildResultAssetManifestEntry(BaseModel):
    assetType: StrictStr | None = None
    assetName: StrictStr | None = None
    assetId: StrictStr | None = None
