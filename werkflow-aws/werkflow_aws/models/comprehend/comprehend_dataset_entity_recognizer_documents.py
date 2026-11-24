from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class ComprehendDatasetEntityRecognizerDocuments(BaseModel):
    S3Uri: StrictStr
    InputFormat: Literal['ONE_DOC_PER_FILE', 'ONE_DOC_PER_LINE'] | None = None
