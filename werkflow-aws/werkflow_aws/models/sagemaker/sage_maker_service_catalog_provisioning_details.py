from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_provisioning_parameter import SageMakerProvisioningParameter


class SageMakerServiceCatalogProvisioningDetails(BaseModel):
    ProductId: StrictStr | None = None
    ProvisioningArtifactId: StrictStr | None = None
    PathId: StrictStr | None = None
    ProvisioningParameters: list[SageMakerProvisioningParameter] | None = None
