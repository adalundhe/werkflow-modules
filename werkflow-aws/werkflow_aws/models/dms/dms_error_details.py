from __future__ import annotations
from pydantic import BaseModel
from .dms_default_error_details import DMSDefaultErrorDetails


class DMSErrorDetails(BaseModel):
    defaultErrorDetails: DMSDefaultErrorDetails | None = None
