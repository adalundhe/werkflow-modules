from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class ComprehendStartDocumentClassificationJobResponse(BaseModel):
    JobId: StrictStr | None = None
    JobArn: StrictStr | None = None
    JobStatus: StrictStr | None = None
    DocumentClassifierArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
