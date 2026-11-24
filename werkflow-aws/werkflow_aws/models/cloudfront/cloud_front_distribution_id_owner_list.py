from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .cloud_front_distribution_id_owner import CloudFrontDistributionIdOwner


class CloudFrontDistributionIdOwnerList(BaseModel):
    Marker: StrictStr | None = None
    NextMarker: StrictStr | None = None
    MaxItems: StrictInt | None = None
    IsTruncated: StrictBool | None = None
    Quantity: StrictInt | None = None
    Items: list[CloudFrontDistributionIdOwner] | None = None
