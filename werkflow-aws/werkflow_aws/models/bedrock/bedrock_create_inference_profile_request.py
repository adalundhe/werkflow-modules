from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .bedrock_inference_profile_model_source import BedrockInferenceProfileModelSource
from .bedrock_tag import BedrockTag


class BedrockCreateInferenceProfileRequest(BaseModel):
    inferenceProfileName: StrictStr
    modelSource: BedrockInferenceProfileModelSource
    description: StrictStr | None = None
    clientRequestToken: StrictStr | None = None
    tags: list[BedrockTag] | None = None
