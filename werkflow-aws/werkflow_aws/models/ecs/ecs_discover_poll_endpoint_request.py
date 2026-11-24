from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECSDiscoverPollEndpointRequest(BaseModel):
    containerInstance: StrictStr | None = None
    cluster: StrictStr | None = None
