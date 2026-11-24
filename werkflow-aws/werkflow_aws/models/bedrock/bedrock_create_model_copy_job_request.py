from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .bedrock_tag import BedrockTag


class BedrockCreateModelCopyJobRequest(BaseModel):
    sourceModelArn: StrictStr
    targetModelName: StrictStr
    modelKmsKeyId: StrictStr | None = None
    targetModelTags: list[BedrockTag] | None = None
    clientRequestToken: StrictStr | None = None
