from __future__ import annotations
from pydantic import BaseModel
from .ec2_resource_statement_request import EC2ResourceStatementRequest


class EC2ThroughResourcesStatementRequest(BaseModel):
    ResourceStatement: EC2ResourceStatementRequest | None = None
