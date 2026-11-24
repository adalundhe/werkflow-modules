from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ComprehendStopTrainingDocumentClassifierRequest(BaseModel):
    DocumentClassifierArn: StrictStr
