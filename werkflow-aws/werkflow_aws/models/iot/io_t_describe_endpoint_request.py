from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTDescribeEndpointRequest(BaseModel):
    endpointType: StrictStr | None = None
