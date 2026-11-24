from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .service_catalog_tag import ServiceCatalogTag
from .service_catalog_update_provisioning_parameter import ServiceCatalogUpdateProvisioningParameter
from .service_catalog_update_provisioning_preferences import ServiceCatalogUpdateProvisioningPreferences


class ServiceCatalogUpdateProvisionedProductRequest(BaseModel):
    UpdateToken: StrictStr
    AcceptLanguage: StrictStr | None = None
    ProvisionedProductName: StrictStr | None = None
    ProvisionedProductId: StrictStr | None = None
    ProductId: StrictStr | None = None
    ProductName: StrictStr | None = None
    ProvisioningArtifactId: StrictStr | None = None
    ProvisioningArtifactName: StrictStr | None = None
    PathId: StrictStr | None = None
    PathName: StrictStr | None = None
    ProvisioningParameters: list[ServiceCatalogUpdateProvisioningParameter] | None = None
    ProvisioningPreferences: ServiceCatalogUpdateProvisioningPreferences | None = None
    Tags: list[ServiceCatalogTag] | None = None
