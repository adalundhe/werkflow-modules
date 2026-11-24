from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .route53_collection_summary import Route53CollectionSummary


class Route53ListCidrCollectionsResponse(BaseModel):
    NextToken: StrictStr | None = None
    CidrCollections: list[Route53CollectionSummary] | None = None
    ResponseMetadata: dict[str, Any] | None = None
