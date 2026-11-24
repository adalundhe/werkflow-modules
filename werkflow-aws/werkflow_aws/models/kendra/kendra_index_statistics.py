from __future__ import annotations
from pydantic import BaseModel
from .kendra_faq_statistics import KendraFaqStatistics
from .kendra_text_document_statistics import KendraTextDocumentStatistics


class KendraIndexStatistics(BaseModel):
    FaqStatistics: KendraFaqStatistics | None = None
    TextDocumentStatistics: KendraTextDocumentStatistics | None = None
