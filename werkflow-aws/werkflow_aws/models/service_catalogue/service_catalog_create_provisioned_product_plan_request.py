from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .service_catalog_tag import ServiceCatalogTag
from .service_catalog_update_provisioning_parameter import ServiceCatalogUpdateProvisioningParameter


class ServiceCatalogCreateProvisionedProductPlanRequest(BaseModel):
    PlanName: StrictStr
    PlanType: Literal['CLOUDFORMATION']
    ProductId: StrictStr
    ProvisionedProductName: StrictStr
    ProvisioningArtifactId: StrictStr
    IdempotencyToken: StrictStr
    AcceptLanguage: StrictStr | None = None
    NotificationArns: list[StrictStr] | None = None
    PathId: StrictStr | None = None
    ProvisioningParameters: list[ServiceCatalogUpdateProvisioningParameter] | None = None
    Tags: list[ServiceCatalogTag] | None = None
