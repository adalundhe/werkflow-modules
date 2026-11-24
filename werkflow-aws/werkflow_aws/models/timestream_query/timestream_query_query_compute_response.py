from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .timestream_query_provisioned_capacity_response import TimestreamQueryProvisionedCapacityResponse


class TimestreamQueryQueryComputeResponse(BaseModel):
    ComputeMode: StrictStr | None = None
    ProvisionedCapacity: TimestreamQueryProvisionedCapacityResponse | None = None
