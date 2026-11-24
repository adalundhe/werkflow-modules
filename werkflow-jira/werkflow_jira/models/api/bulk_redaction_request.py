from __future__ import annotations
from pydantic import BaseModel
from .single_redaction_request import SingleRedactionRequest


class BulkRedactionRequest(BaseModel):
    redactions: list[SingleRedactionRequest] | None = None
