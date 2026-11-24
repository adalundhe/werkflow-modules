from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class SSMNodeAggregator(BaseModel):
    AggregatorType: Literal['Count']
    TypeName: Literal['Instance']
    AttributeName: Literal['AgentVersion', 'PlatformName', 'PlatformType', 'PlatformVersion', 'Region', 'ResourceType', 'SourceType', 'AvailabilityZone']
    Aggregators: list[SSMNodeAggregator] | None = None
