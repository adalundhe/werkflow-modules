from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr


class ServiceCatalogProvisioningArtifactProperties(BaseModel):
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    Info: dict[StrictStr, StrictStr] | None = None
    Type: Literal['CLOUD_FORMATION_TEMPLATE', 'MARKETPLACE_AMI', 'MARKETPLACE_CAR', 'TERRAFORM_OPEN_SOURCE', 'TERRAFORM_CLOUD', 'EXTERNAL'] | None = None
    DisableTemplateValidation: StrictBool | None = None
