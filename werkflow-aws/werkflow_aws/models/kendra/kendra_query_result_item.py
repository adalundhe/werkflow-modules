from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .kendra_additional_result_attribute import KendraAdditionalResultAttribute
from .kendra_collapsed_result_detail import KendraCollapsedResultDetail
from .kendra_document_attribute import KendraDocumentAttribute
from .kendra_score_attributes import KendraScoreAttributes
from .kendra_table_excerpt import KendraTableExcerpt
from .kendra_text_with_highlights import KendraTextWithHighlights


class KendraQueryResultItem(BaseModel):
    Id: StrictStr | None = None
    Type: StrictStr | None = None
    Format: StrictStr | None = None
    AdditionalAttributes: list[KendraAdditionalResultAttribute] | None = None
    DocumentId: StrictStr | None = None
    DocumentTitle: KendraTextWithHighlights | None = None
    DocumentExcerpt: KendraTextWithHighlights | None = None
    DocumentURI: StrictStr | None = None
    DocumentAttributes: list[KendraDocumentAttribute] | None = None
    ScoreAttributes: KendraScoreAttributes | None = None
    FeedbackToken: StrictStr | None = None
    TableExcerpt: KendraTableExcerpt | None = None
    CollapsedResultDetail: KendraCollapsedResultDetail | None = None
