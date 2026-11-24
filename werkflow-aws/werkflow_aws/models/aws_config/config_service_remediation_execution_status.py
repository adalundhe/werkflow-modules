from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .config_service_remediation_execution_step import ConfigServiceRemediationExecutionStep
from .config_service_resource_key import ConfigServiceResourceKey


class ConfigServiceRemediationExecutionStatus(BaseModel):
    ResourceKey: ConfigServiceResourceKey | None = None
    State: StrictStr | None = None
    StepDetails: list[ConfigServiceRemediationExecutionStep] | None = None
    InvocationTime: datetime.datetime | StrictStr | None = None
    LastUpdatedTime: datetime.datetime | StrictStr | None = None
