from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .bedrock_tag import BedrockTag


class BedrockCreateProvisionedModelThroughputRequest(BaseModel):
    modelUnits: StrictInt
    provisionedModelName: StrictStr
    modelId: StrictStr
    clientRequestToken: StrictStr | None = None
    commitmentDuration: Literal['OneMonth', 'SixMonths'] | None = None
    tags: list[BedrockTag] | None = None
