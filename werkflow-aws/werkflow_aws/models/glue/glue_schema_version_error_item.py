from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .glue_error_details import GlueErrorDetails


class GlueSchemaVersionErrorItem(BaseModel):
    VersionNumber: StrictInt | None = None
    ErrorDetails: GlueErrorDetails | None = None
