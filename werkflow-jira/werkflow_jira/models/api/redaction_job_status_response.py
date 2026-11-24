from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .bulk_redaction_response import BulkRedactionResponse


class RedactionJobStatusResponse(BaseModel):
    bulkRedactionResponse: BulkRedactionResponse | None = None
    jobStatus: StrictStr | None = None
