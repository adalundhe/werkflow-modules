from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .kendra_featured_document import KendraFeaturedDocument
from .kendra_tag import KendraTag


class KendraCreateFeaturedResultsSetRequest(BaseModel):
    IndexId: StrictStr
    FeaturedResultsSetName: StrictStr
    Description: StrictStr | None = None
    ClientToken: StrictStr | None = None
    Status: Literal['ACTIVE', 'INACTIVE'] | None = None
    QueryTexts: list[StrictStr] | None = None
    FeaturedDocuments: list[KendraFeaturedDocument] | None = None
    Tags: list[KendraTag] | None = None
