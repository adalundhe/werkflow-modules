from __future__ import annotations
from typing import BinaryIO
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictStr
from .comprehend_document_reader_config import ComprehendDocumentReaderConfig


class ComprehendClassifyDocumentRequest(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    EndpointArn: StrictStr
    Text: StrictStr | None = None
    Bytes: StrictBytes | BinaryIO | StrictStr | None = None
    DocumentReaderConfig: ComprehendDocumentReaderConfig | None = None
