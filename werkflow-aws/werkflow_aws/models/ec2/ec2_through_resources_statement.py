from __future__ import annotations
from pydantic import BaseModel
from .ec2_resource_statement import EC2ResourceStatement


class EC2ThroughResourcesStatement(BaseModel):
    ResourceStatement: EC2ResourceStatement | None = None
