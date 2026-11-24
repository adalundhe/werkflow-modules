from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_formation_warning_property import CloudFormationWarningProperty


class CloudFormationWarningDetail(BaseModel):
    Type: StrictStr | None = None
    Properties: list[CloudFormationWarningProperty] | None = None
