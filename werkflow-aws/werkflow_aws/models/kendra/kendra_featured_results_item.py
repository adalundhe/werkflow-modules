from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .kendra_additional_result_attribute import KendraAdditionalResultAttribute
from .kendra_document_attribute import KendraDocumentAttribute
from .kendra_text_with_highlights import KendraTextWithHighlights


class KendraFeaturedResultsItem(BaseModel):
    Id: StrictStr | None = None
    Type: StrictStr | None = None
    AdditionalAttributes: list[KendraAdditionalResultAttribute] | None = None
    DocumentId: StrictStr | None = None
    DocumentTitle: KendraTextWithHighlights | None = None
    DocumentExcerpt: KendraTextWithHighlights | None = None
    DocumentURI: StrictStr | None = None
    DocumentAttributes: list[KendraDocumentAttribute] | None = None
    FeedbackToken: StrictStr | None = None
