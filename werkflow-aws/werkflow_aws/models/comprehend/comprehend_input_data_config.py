from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .comprehend_document_reader_config import ComprehendDocumentReaderConfig


class ComprehendInputDataConfig(BaseModel):
    S3Uri: StrictStr | None = None
    InputFormat: StrictStr | None = None
    DocumentReaderConfig: ComprehendDocumentReaderConfig | None = None
