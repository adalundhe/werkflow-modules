from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .kendra_document_attribute import KendraDocumentAttribute
from .kendra_text_with_highlights import KendraTextWithHighlights


class KendraExpandedResultItem(BaseModel):
    Id: StrictStr | None = None
    DocumentId: StrictStr | None = None
    DocumentTitle: KendraTextWithHighlights | None = None
    DocumentExcerpt: KendraTextWithHighlights | None = None
    DocumentURI: StrictStr | None = None
    DocumentAttributes: list[KendraDocumentAttribute] | None = None
