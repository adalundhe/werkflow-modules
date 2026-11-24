from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ComprehendDatasetDocumentClassifierInputDataConfig(BaseModel):
    S3Uri: StrictStr
    LabelDelimiter: StrictStr | None = None
