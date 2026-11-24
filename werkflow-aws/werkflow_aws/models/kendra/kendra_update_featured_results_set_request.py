from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .kendra_featured_document import KendraFeaturedDocument


class KendraUpdateFeaturedResultsSetRequest(BaseModel):
    IndexId: StrictStr
    FeaturedResultsSetId: StrictStr
    FeaturedResultsSetName: StrictStr | None = None
    Description: StrictStr | None = None
    Status: Literal['ACTIVE', 'INACTIVE'] | None = None
    QueryTexts: list[StrictStr] | None = None
    FeaturedDocuments: list[KendraFeaturedDocument] | None = None
