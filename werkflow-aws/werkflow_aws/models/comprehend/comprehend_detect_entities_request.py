from __future__ import annotations
from typing import BinaryIO, Literal
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictStr
from .comprehend_document_reader_config import ComprehendDocumentReaderConfig


class ComprehendDetectEntitiesRequest(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    Text: StrictStr | None = None
    LanguageCode: Literal['en', 'es', 'fr', 'de', 'it', 'pt', 'ar', 'hi', 'ja', 'ko', 'zh', 'zh-TW'] | None = None
    EndpointArn: StrictStr | None = None
    Bytes: StrictBytes | BinaryIO | StrictStr | None = None
    DocumentReaderConfig: ComprehendDocumentReaderConfig | None = None
