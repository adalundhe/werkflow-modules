from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .service_catalog_provisioning_parameter import ServiceCatalogProvisioningParameter
from .service_catalog_provisioning_preferences import ServiceCatalogProvisioningPreferences
from .service_catalog_tag import ServiceCatalogTag


class ServiceCatalogProvisionProductRequest(BaseModel):
    ProvisionedProductName: StrictStr
    ProvisionToken: StrictStr
    AcceptLanguage: StrictStr | None = None
    ProductId: StrictStr | None = None
    ProductName: StrictStr | None = None
    ProvisioningArtifactId: StrictStr | None = None
    ProvisioningArtifactName: StrictStr | None = None
    PathId: StrictStr | None = None
    PathName: StrictStr | None = None
    ProvisioningParameters: list[ServiceCatalogProvisioningParameter] | None = None
    ProvisioningPreferences: ServiceCatalogProvisioningPreferences | None = None
    Tags: list[ServiceCatalogTag] | None = None
    NotificationArns: list[StrictStr] | None = None
