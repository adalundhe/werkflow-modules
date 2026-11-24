from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .bedrock_additional_model_request_fields_value import BedrockAdditionalModelRequestFieldsValue
from .bedrock_inference_configuration import BedrockInferenceConfiguration


class BedrockModelConfiguration(BaseModel):
    modelId: StrictStr | None = None
    inferenceConfig: BedrockInferenceConfiguration | None = None
    additionalModelRequestFields: dict[StrictStr, BedrockAdditionalModelRequestFieldsValue] | None = None
