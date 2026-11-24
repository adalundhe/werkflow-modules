from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .bedrock_external_source import BedrockExternalSource
from .bedrock_external_sources_generation_configuration import BedrockExternalSourcesGenerationConfiguration


class BedrockExternalSourcesRetrieveAndGenerateConfiguration(BaseModel):
    modelArn: StrictStr | None = None
    sources: list[BedrockExternalSource] | None = None
    generationConfiguration: BedrockExternalSourcesGenerationConfiguration | None = None
