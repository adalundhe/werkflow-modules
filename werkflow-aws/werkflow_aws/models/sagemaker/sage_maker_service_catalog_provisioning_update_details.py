from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_provisioning_parameter import SageMakerProvisioningParameter


class SageMakerServiceCatalogProvisioningUpdateDetails(BaseModel):
    ProvisioningArtifactId: StrictStr | None = None
    ProvisioningParameters: list[SageMakerProvisioningParameter] | None = None
