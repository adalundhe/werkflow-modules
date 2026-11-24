from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .cloud_front_distribution_tenant_association_filter import CloudFrontDistributionTenantAssociationFilter


class CloudFrontListDistributionTenantsRequest(BaseModel):
    AssociationFilter: CloudFrontDistributionTenantAssociationFilter | None = None
    Marker: StrictStr | None = None
    MaxItems: StrictInt | None = None
