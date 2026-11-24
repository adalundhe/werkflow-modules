from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .kendra_document_attribute import KendraDocumentAttribute
from .kendra_score_attributes import KendraScoreAttributes


class KendraRetrieveResultItem(BaseModel):
    Id: StrictStr | None = None
    DocumentId: StrictStr | None = None
    DocumentTitle: StrictStr | None = None
    Content: StrictStr | None = None
    DocumentURI: StrictStr | None = None
    DocumentAttributes: list[KendraDocumentAttribute] | None = None
    ScoreAttributes: KendraScoreAttributes | None = None
