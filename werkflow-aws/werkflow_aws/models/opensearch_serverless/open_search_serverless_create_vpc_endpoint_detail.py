from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchServerlessCreateVpcEndpointDetail(BaseModel):
    id: StrictStr | None = None
    name: StrictStr | None = None
    status: StrictStr | None = None
