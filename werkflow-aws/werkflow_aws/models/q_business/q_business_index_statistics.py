from __future__ import annotations
from pydantic import BaseModel
from .q_business_text_document_statistics import QBusinessTextDocumentStatistics


class QBusinessIndexStatistics(BaseModel):
    textDocumentStatistics: QBusinessTextDocumentStatistics | None = None
