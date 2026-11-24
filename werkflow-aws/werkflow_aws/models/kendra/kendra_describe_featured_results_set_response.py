from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .kendra_featured_document_missing import KendraFeaturedDocumentMissing
from .kendra_featured_document_with_metadata import KendraFeaturedDocumentWithMetadata


class KendraDescribeFeaturedResultsSetResponse(BaseModel):
    FeaturedResultsSetId: StrictStr | None = None
    FeaturedResultsSetName: StrictStr | None = None
    Description: StrictStr | None = None
    Status: StrictStr | None = None
    QueryTexts: list[StrictStr] | None = None
    FeaturedDocumentsWithMetadata: list[KendraFeaturedDocumentWithMetadata] | None = None
    FeaturedDocumentsMissing: list[KendraFeaturedDocumentMissing] | None = None
    LastUpdatedTimestamp: StrictInt | None = None
    CreationTimestamp: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
