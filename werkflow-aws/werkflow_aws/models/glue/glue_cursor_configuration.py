from __future__ import annotations
from pydantic import BaseModel
from .glue_extracted_parameter import GlueExtractedParameter


class GlueCursorConfiguration(BaseModel):
    NextPage: GlueExtractedParameter | None = None
    LimitParameter: GlueExtractedParameter | None = None
