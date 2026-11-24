from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_front_distribution_resource_id import CloudFrontDistributionResourceId


class CloudFrontUpdateDomainAssociationRequest(BaseModel):
    Domain: StrictStr
    TargetResource: CloudFrontDistributionResourceId
    IfMatch: StrictStr | None = None
