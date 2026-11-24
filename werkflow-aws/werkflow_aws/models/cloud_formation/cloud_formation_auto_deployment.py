from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class CloudFormationAutoDeployment(BaseModel):
    Enabled: StrictBool | None = None
    RetainStacksOnAccountRemoval: StrictBool | None = None
    DependsOn: list[StrictStr] | None = None
