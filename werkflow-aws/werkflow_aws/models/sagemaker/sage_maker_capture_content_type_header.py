from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerCaptureContentTypeHeader(BaseModel):
    CsvContentTypes: list[StrictStr] | None = None
    JsonContentTypes: list[StrictStr] | None = None
