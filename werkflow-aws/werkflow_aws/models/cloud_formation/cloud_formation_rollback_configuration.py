from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .cloud_formation_rollback_trigger import CloudFormationRollbackTrigger


class CloudFormationRollbackConfiguration(BaseModel):
    RollbackTriggers: list[CloudFormationRollbackTrigger] | None = None
    MonitoringTimeInMinutes: StrictInt | None = None
