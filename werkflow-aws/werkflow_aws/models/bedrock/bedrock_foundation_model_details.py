from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .bedrock_foundation_model_lifecycle import BedrockFoundationModelLifecycle


class BedrockFoundationModelDetails(BaseModel):
    modelArn: StrictStr | None = None
    modelId: StrictStr | None = None
    modelName: StrictStr | None = None
    providerName: StrictStr | None = None
    inputModalities: list[StrictStr] | None = None
    outputModalities: list[StrictStr] | None = None
    responseStreamingSupported: StrictBool | None = None
    customizationsSupported: list[StrictStr] | None = None
    inferenceTypesSupported: list[StrictStr] | None = None
    modelLifecycle: BedrockFoundationModelLifecycle | None = None
