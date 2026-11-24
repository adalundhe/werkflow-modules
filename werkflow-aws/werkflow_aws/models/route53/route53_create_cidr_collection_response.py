from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .route53_cidr_collection import Route53CidrCollection


class Route53CreateCidrCollectionResponse(BaseModel):
    Collection: Route53CidrCollection | None = None
    Location: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
