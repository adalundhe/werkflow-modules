from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class SSMNodeFilter(BaseModel):
    Key: Literal['AgentType', 'AgentVersion', 'ComputerName', 'InstanceId', 'InstanceStatus', 'IpAddress', 'ManagedStatus', 'PlatformName', 'PlatformType', 'PlatformVersion', 'ResourceType', 'OrganizationalUnitId', 'OrganizationalUnitPath', 'Region', 'AccountId', 'SourceType', 'SourceId', 'SourceLocation', 'AvailabilityZone', 'AvailabilityZoneId']
    Values: list[StrictStr]
    Type: Literal['Equal', 'NotEqual', 'BeginWith'] | None = None
