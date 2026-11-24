from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .cloud_front_streaming_distribution_summary import CloudFrontStreamingDistributionSummary


class CloudFrontStreamingDistributionList(BaseModel):
    Marker: StrictStr | None = None
    NextMarker: StrictStr | None = None
    MaxItems: StrictInt | None = None
    IsTruncated: StrictBool | None = None
    Quantity: StrictInt | None = None
    Items: list[CloudFrontStreamingDistributionSummary] | None = None
