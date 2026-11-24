from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .cloud_front_conflicting_alias import CloudFrontConflictingAlias


class CloudFrontConflictingAliasesList(BaseModel):
    NextMarker: StrictStr | None = None
    MaxItems: StrictInt | None = None
    Quantity: StrictInt | None = None
    Items: list[CloudFrontConflictingAlias] | None = None
