from __future__ import annotations
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from .bedrock_runtime_document import BedrockRuntimeDocument
from .bedrock_runtime_document_block import BedrockRuntimeDocumentBlock
from .bedrock_runtime_image_block import BedrockRuntimeImageBlock
from .bedrock_runtime_search_result_block import BedrockRuntimeSearchResultBlock
from .bedrock_runtime_video_block import BedrockRuntimeVideoBlock


class BedrockRuntimeToolResultContentBlock(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    json_: BedrockRuntimeDocument | None = Field(default=None, alias='json')
    text: StrictStr | None = None
    image: BedrockRuntimeImageBlock | None = None
    document: BedrockRuntimeDocumentBlock | None = None
    video: BedrockRuntimeVideoBlock | None = None
    searchResult: BedrockRuntimeSearchResultBlock | None = None
