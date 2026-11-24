from __future__ import annotations
from pydantic import BaseModel
from .ec2_path_statement_request import EC2PathStatementRequest
from .ec2_through_resources_statement_request import EC2ThroughResourcesStatementRequest


class EC2AccessScopePathRequest(BaseModel):
    Source: EC2PathStatementRequest | None = None
    Destination: EC2PathStatementRequest | None = None
    ThroughResources: list[EC2ThroughResourcesStatementRequest] | None = None
