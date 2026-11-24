from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .service_catalog_parameter_constraints import ServiceCatalogParameterConstraints


class ServiceCatalogProvisioningArtifactParameter(BaseModel):
    ParameterKey: StrictStr | None = None
    DefaultValue: StrictStr | None = None
    ParameterType: StrictStr | None = None
    IsNoEcho: StrictBool | None = None
    Description: StrictStr | None = None
    ParameterConstraints: ServiceCatalogParameterConstraints | None = None
