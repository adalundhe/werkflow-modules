from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_resource_spec import SageMakerResourceSpec


class SageMakerRStudioServerProDomainSettingsForUpdate(BaseModel):
    DomainExecutionRoleArn: StrictStr
    DefaultResourceSpec: SageMakerResourceSpec | None = None
    RStudioConnectUrl: StrictStr | None = None
    RStudioPackageManagerUrl: StrictStr | None = None
