from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .comprehend_document_class import ComprehendDocumentClass
from .comprehend_document_label import ComprehendDocumentLabel
from .comprehend_document_metadata import ComprehendDocumentMetadata
from .comprehend_document_type_list_item import ComprehendDocumentTypeListItem
from .comprehend_errors_list_item import ComprehendErrorsListItem
from .comprehend_warnings_list_item import ComprehendWarningsListItem


class ComprehendClassifyDocumentResponse(BaseModel):
    Classes: list[ComprehendDocumentClass] | None = None
    Labels: list[ComprehendDocumentLabel] | None = None
    DocumentMetadata: ComprehendDocumentMetadata | None = None
    DocumentType: list[ComprehendDocumentTypeListItem] | None = None
    Errors: list[ComprehendErrorsListItem] | None = None
    Warnings: list[ComprehendWarningsListItem] | None = None
    ResponseMetadata: dict[str, Any] | None = None
