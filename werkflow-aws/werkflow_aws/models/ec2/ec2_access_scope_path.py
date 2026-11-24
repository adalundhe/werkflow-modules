from __future__ import annotations
from pydantic import BaseModel
from .ec2_path_statement import EC2PathStatement
from .ec2_through_resources_statement import EC2ThroughResourcesStatement


class EC2AccessScopePath(BaseModel):
    Source: EC2PathStatement | None = None
    Destination: EC2PathStatement | None = None
    ThroughResources: list[EC2ThroughResourcesStatement] | None = None
