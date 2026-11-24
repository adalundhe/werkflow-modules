from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .route53_cidr_collection_change import Route53CidrCollectionChange


class Route53ChangeCidrCollectionRequest(BaseModel):
    Id: StrictStr
    Changes: list[Route53CidrCollectionChange]
    CollectionVersion: StrictInt | None = None
