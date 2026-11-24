from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ComprehendDescribeDocumentClassifierRequest(BaseModel):
    DocumentClassifierArn: StrictStr
