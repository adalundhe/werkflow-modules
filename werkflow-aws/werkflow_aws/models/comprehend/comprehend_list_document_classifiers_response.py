from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .comprehend_document_classifier_properties import ComprehendDocumentClassifierProperties


class ComprehendListDocumentClassifiersResponse(BaseModel):
    DocumentClassifierPropertiesList: list[ComprehendDocumentClassifierProperties] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
