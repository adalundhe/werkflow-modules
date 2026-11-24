from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .bedrock_byte_content_doc import BedrockByteContentDoc
from .bedrock_s3_object_doc import BedrockS3ObjectDoc


class BedrockExternalSource(BaseModel):
    sourceType: StrictStr | None = None
    s3Location: BedrockS3ObjectDoc | None = None
    byteContent: BedrockByteContentDoc | None = None
