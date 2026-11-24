from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .bedrock_additional_model_request_fields_value import BedrockAdditionalModelRequestFieldsValue


class BedrockVectorSearchBedrockRerankingModelConfiguration(BaseModel):
    modelArn: StrictStr | None = None
    additionalModelRequestFields: dict[StrictStr, BedrockAdditionalModelRequestFieldsValue] | None = None
