from __future__ import annotations
from pydantic import BaseModel
from .single_redaction_response import SingleRedactionResponse


class BulkRedactionResponse(BaseModel):
    results: list[SingleRedactionResponse] | None = None
