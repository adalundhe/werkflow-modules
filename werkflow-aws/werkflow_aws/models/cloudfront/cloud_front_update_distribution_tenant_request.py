from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .cloud_front_customizations import CloudFrontCustomizations
from .cloud_front_domain_item import CloudFrontDomainItem
from .cloud_front_managed_certificate_request import CloudFrontManagedCertificateRequest
from .cloud_front_parameter import CloudFrontParameter


class CloudFrontUpdateDistributionTenantRequest(BaseModel):
    Id: StrictStr
    IfMatch: StrictStr
    DistributionId: StrictStr | None = None
    Domains: list[CloudFrontDomainItem] | None = None
    Customizations: CloudFrontCustomizations | None = None
    Parameters: list[CloudFrontParameter] | None = None
    ConnectionGroupId: StrictStr | None = None
    ManagedCertificateRequest: CloudFrontManagedCertificateRequest | None = None
    Enabled: StrictBool | None = None
    OnDomainTakeover: Literal['allow', 'reject'] | None = None
