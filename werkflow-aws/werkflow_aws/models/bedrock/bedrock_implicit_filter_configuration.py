from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .bedrock_metadata_attribute_schema import BedrockMetadataAttributeSchema


class BedrockImplicitFilterConfiguration(BaseModel):
    metadataAttributes: list[BedrockMetadataAttributeSchema] | None = None
    modelArn: StrictStr | None = None
