from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerCaptureContentTypeHeaderModel(BaseModel):
    CsvContentTypes: list[StrictStr] | None = None
    JsonContentTypes: list[StrictStr] | None = None
