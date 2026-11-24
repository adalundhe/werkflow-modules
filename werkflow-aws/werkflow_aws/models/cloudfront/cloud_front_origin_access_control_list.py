from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .cloud_front_origin_access_control_summary import CloudFrontOriginAccessControlSummary


class CloudFrontOriginAccessControlList(BaseModel):
    Marker: StrictStr | None = None
    NextMarker: StrictStr | None = None
    MaxItems: StrictInt | None = None
    IsTruncated: StrictBool | None = None
    Quantity: StrictInt | None = None
    Items: list[CloudFrontOriginAccessControlSummary] | None = None
