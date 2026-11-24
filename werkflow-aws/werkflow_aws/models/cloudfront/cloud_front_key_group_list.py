from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .cloud_front_key_group_summary import CloudFrontKeyGroupSummary


class CloudFrontKeyGroupList(BaseModel):
    NextMarker: StrictStr | None = None
    MaxItems: StrictInt | None = None
    Quantity: StrictInt | None = None
    Items: list[CloudFrontKeyGroupSummary] | None = None
