from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class CloudFormationDeploymentConfig(BaseModel):
    Mode: StrictStr | None = None
    DisableRollback: StrictBool | None = None
