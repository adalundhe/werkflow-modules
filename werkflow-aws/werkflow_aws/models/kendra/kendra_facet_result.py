from __future__ import annotations
from typing import TYPE_CHECKING
from pydantic import BaseModel, StrictStr

if TYPE_CHECKING:
    from .kendra_document_attribute_value_count_pair import KendraDocumentAttributeValueCountPair


class KendraFacetResult(BaseModel):
    DocumentAttributeKey: StrictStr | None = None
    DocumentAttributeValueType: StrictStr | None = None
    DocumentAttributeValueCountPairs: list[KendraDocumentAttributeValueCountPair] | None = None
