from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class SageMakerUpdateMlflowAppRequest(BaseModel):
    Arn: StrictStr
    Name: StrictStr | None = None
    ArtifactStoreUri: StrictStr | None = None
    ModelRegistrationMode: Literal['AutoModelRegistrationEnabled', 'AutoModelRegistrationDisabled'] | None = None
    WeeklyMaintenanceWindowStart: StrictStr | None = None
    DefaultDomainIdList: list[StrictStr] | None = None
    AccountDefaultStatus: Literal['ENABLED', 'DISABLED'] | None = None
