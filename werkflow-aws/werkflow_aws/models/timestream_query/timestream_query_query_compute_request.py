from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .timestream_query_provisioned_capacity_request import TimestreamQueryProvisionedCapacityRequest


class TimestreamQueryQueryComputeRequest(BaseModel):
    ComputeMode: Literal['ON_DEMAND', 'PROVISIONED'] | None = None
    ProvisionedCapacity: TimestreamQueryProvisionedCapacityRequest | None = None
