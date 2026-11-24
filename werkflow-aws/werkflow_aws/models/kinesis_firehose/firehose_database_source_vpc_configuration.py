from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FirehoseDatabaseSourceVPCConfiguration(BaseModel):
    VpcEndpointServiceName: StrictStr | None = None
