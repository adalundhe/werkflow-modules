from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .cloud_front_vpc_origin_summary import CloudFrontVpcOriginSummary


class CloudFrontVpcOriginList(BaseModel):
    Marker: StrictStr | None = None
    NextMarker: StrictStr | None = None
    MaxItems: StrictInt | None = None
    IsTruncated: StrictBool | None = None
    Quantity: StrictInt | None = None
    Items: list[CloudFrontVpcOriginSummary] | None = None
