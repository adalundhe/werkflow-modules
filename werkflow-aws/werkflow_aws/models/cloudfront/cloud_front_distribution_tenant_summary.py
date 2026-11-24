from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr
from .cloud_front_customizations import CloudFrontCustomizations
from .cloud_front_domain_result import CloudFrontDomainResult


class CloudFrontDistributionTenantSummary(BaseModel):
    Id: StrictStr | None = None
    DistributionId: StrictStr | None = None
    Name: StrictStr | None = None
    Arn: StrictStr | None = None
    Domains: list[CloudFrontDomainResult] | None = None
    ConnectionGroupId: StrictStr | None = None
    Customizations: CloudFrontCustomizations | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    ETag: StrictStr | None = None
    Enabled: StrictBool | None = None
    Status: StrictStr | None = None
