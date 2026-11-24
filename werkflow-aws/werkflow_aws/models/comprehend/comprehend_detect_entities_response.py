from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .comprehend_block import ComprehendBlock
from .comprehend_document_metadata import ComprehendDocumentMetadata
from .comprehend_document_type_list_item import ComprehendDocumentTypeListItem
from .comprehend_entity import ComprehendEntity
from .comprehend_errors_list_item import ComprehendErrorsListItem


class ComprehendDetectEntitiesResponse(BaseModel):
    Entities: list[ComprehendEntity] | None = None
    DocumentMetadata: ComprehendDocumentMetadata | None = None
    DocumentType: list[ComprehendDocumentTypeListItem] | None = None
    Blocks: list[ComprehendBlock] | None = None
    Errors: list[ComprehendErrorsListItem] | None = None
    ResponseMetadata: dict[str, Any] | None = None
