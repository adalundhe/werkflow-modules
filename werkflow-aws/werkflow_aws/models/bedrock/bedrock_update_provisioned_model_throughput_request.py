from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockUpdateProvisionedModelThroughputRequest(BaseModel):
    provisionedModelId: StrictStr
    desiredProvisionedModelName: StrictStr | None = None
    desiredModelId: StrictStr | None = None
