from __future__ import annotations
from pydantic import BaseModel
from .glue_extracted_parameter import GlueExtractedParameter


class GlueOffsetConfiguration(BaseModel):
    OffsetParameter: GlueExtractedParameter | None = None
    LimitParameter: GlueExtractedParameter | None = None
