from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class ServiceCatalogDescribeProvisioningArtifactRequest(BaseModel):
    AcceptLanguage: StrictStr | None = None
    ProvisioningArtifactId: StrictStr | None = None
    ProductId: StrictStr | None = None
    ProvisioningArtifactName: StrictStr | None = None
    ProductName: StrictStr | None = None
    Verbose: StrictBool | None = None
    IncludeProvisioningArtifactParameters: StrictBool | None = None
