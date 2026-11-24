from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .bedrock_runtime_async_invoke_output_data_config import BedrockRuntimeAsyncInvokeOutputDataConfig
from .bedrock_runtime_model_input_payload import BedrockRuntimeModelInputPayload
from .bedrock_runtime_tag import BedrockRuntimeTag


class BedrockRuntimeStartAsyncInvokeRequest(BaseModel):
    modelId: StrictStr
    modelInput: BedrockRuntimeModelInputPayload
    outputDataConfig: BedrockRuntimeAsyncInvokeOutputDataConfig
    clientRequestToken: StrictStr | None = None
    tags: list[BedrockRuntimeTag] | None = None
