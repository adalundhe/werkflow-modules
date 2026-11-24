from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .kendra_featured_document import KendraFeaturedDocument


class KendraFeaturedResultsSet(BaseModel):
    FeaturedResultsSetId: StrictStr | None = None
    FeaturedResultsSetName: StrictStr | None = None
    Description: StrictStr | None = None
    Status: StrictStr | None = None
    QueryTexts: list[StrictStr] | None = None
    FeaturedDocuments: list[KendraFeaturedDocument] | None = None
    LastUpdatedTimestamp: StrictInt | None = None
    CreationTimestamp: StrictInt | None = None
