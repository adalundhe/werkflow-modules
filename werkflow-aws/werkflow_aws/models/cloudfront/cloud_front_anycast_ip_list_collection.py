from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .cloud_front_anycast_ip_list_summary import CloudFrontAnycastIpListSummary


class CloudFrontAnycastIpListCollection(BaseModel):
    Items: list[CloudFrontAnycastIpListSummary] | None = None
    Marker: StrictStr | None = None
    NextMarker: StrictStr | None = None
    MaxItems: StrictInt | None = None
    IsTruncated: StrictBool | None = None
    Quantity: StrictInt | None = None
