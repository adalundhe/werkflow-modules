from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_resource_spec import SageMakerResourceSpec


class SageMakerRStudioServerProDomainSettings(BaseModel):
    DomainExecutionRoleArn: StrictStr | None = None
    RStudioConnectUrl: StrictStr | None = None
    RStudioPackageManagerUrl: StrictStr | None = None
    DefaultResourceSpec: SageMakerResourceSpec | None = None
