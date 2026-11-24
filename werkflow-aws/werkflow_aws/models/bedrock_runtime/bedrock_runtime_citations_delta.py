from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .bedrock_runtime_citation_location import BedrockRuntimeCitationLocation
from .bedrock_runtime_citation_source_content_delta import BedrockRuntimeCitationSourceContentDelta


class BedrockRuntimeCitationsDelta(BaseModel):
    title: StrictStr | None = None
    source: StrictStr | None = None
    sourceContent: list[BedrockRuntimeCitationSourceContentDelta] | None = None
    location: BedrockRuntimeCitationLocation | None = None
