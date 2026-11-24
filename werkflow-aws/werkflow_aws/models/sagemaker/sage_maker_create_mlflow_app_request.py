from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .sage_maker_tag_model import SageMakerTagModel


class SageMakerCreateMlflowAppRequest(BaseModel):
    Name: StrictStr
    ArtifactStoreUri: StrictStr
    RoleArn: StrictStr
    KmsKeyId: StrictStr | None = None
    ModelRegistrationMode: Literal['AutoModelRegistrationEnabled', 'AutoModelRegistrationDisabled'] | None = None
    WeeklyMaintenanceWindowStart: StrictStr | None = None
    AccountDefaultStatus: Literal['ENABLED', 'DISABLED'] | None = None
    DefaultDomainIdList: list[StrictStr] | None = None
    Tags: list[SageMakerTagModel] | None = None
