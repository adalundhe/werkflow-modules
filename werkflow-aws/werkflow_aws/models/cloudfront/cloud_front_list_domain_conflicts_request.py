from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .cloud_front_distribution_resource_id import CloudFrontDistributionResourceId


class CloudFrontListDomainConflictsRequest(BaseModel):
    Domain: StrictStr
    DomainControlValidationResource: CloudFrontDistributionResourceId
    MaxItems: StrictInt | None = None
    Marker: StrictStr | None = None
