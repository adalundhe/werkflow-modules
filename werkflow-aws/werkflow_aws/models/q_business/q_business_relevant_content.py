from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .q_business_document_attribute import QBusinessDocumentAttribute
from .q_business_score_attributes import QBusinessScoreAttributes


class QBusinessRelevantContent(BaseModel):
    content: StrictStr | None = None
    documentId: StrictStr | None = None
    documentTitle: StrictStr | None = None
    documentUri: StrictStr | None = None
    documentAttributes: list[QBusinessDocumentAttribute] | None = None
    scoreAttributes: QBusinessScoreAttributes | None = None
