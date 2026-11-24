from __future__ import annotations
from pydantic import BaseModel
from .cloud_formation_regional_stages import CloudFormationRegionalStages


class CloudFormationRegionalStatusDetail(BaseModel):
    Stages: CloudFormationRegionalStages | None = None
