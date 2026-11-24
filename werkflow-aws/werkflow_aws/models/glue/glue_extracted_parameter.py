from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_response_extraction_mapping import GlueResponseExtractionMapping


class GlueExtractedParameter(BaseModel):
    Key: StrictStr | None = None
    DefaultValue: StrictStr | None = None
    PropertyLocation: StrictStr | None = None
    Value: GlueResponseExtractionMapping | None = None
