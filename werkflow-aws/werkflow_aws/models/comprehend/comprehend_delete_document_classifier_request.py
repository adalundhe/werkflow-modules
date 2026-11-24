from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ComprehendDeleteDocumentClassifierRequest(BaseModel):
    DocumentClassifierArn: StrictStr
