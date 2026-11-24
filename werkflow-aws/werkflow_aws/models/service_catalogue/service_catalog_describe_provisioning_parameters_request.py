from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ServiceCatalogDescribeProvisioningParametersRequest(BaseModel):
    AcceptLanguage: StrictStr | None = None
    ProductId: StrictStr | None = None
    ProductName: StrictStr | None = None
    ProvisioningArtifactId: StrictStr | None = None
    ProvisioningArtifactName: StrictStr | None = None
    PathId: StrictStr | None = None
    PathName: StrictStr | None = None
