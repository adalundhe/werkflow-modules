from __future__ import annotations
from pydantic import BaseModel
from .cloud_formation_resource_location import CloudFormationResourceLocation


class CloudFormationResourceMapping(BaseModel):
    Source: CloudFormationResourceLocation | None = None
    Destination: CloudFormationResourceLocation | None = None
