from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ComprehendDescribeDocumentClassificationJobRequest(BaseModel):
    JobId: StrictStr
