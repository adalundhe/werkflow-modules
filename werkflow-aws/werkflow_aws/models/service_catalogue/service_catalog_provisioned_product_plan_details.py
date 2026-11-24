from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .service_catalog_tag import ServiceCatalogTag
from .service_catalog_update_provisioning_parameter import ServiceCatalogUpdateProvisioningParameter


class ServiceCatalogProvisionedProductPlanDetails(BaseModel):
    CreatedTime: datetime.datetime | StrictStr | None = None
    PathId: StrictStr | None = None
    ProductId: StrictStr | None = None
    PlanName: StrictStr | None = None
    PlanId: StrictStr | None = None
    ProvisionProductId: StrictStr | None = None
    ProvisionProductName: StrictStr | None = None
    PlanType: StrictStr | None = None
    ProvisioningArtifactId: StrictStr | None = None
    Status: StrictStr | None = None
    UpdatedTime: datetime.datetime | StrictStr | None = None
    NotificationArns: list[StrictStr] | None = None
    ProvisioningParameters: list[ServiceCatalogUpdateProvisioningParameter] | None = None
    Tags: list[ServiceCatalogTag] | None = None
    StatusMessage: StrictStr | None = None
