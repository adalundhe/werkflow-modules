from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchServerlessDeleteVpcEndpointRequest(BaseModel):
    id: StrictStr
    clientToken: StrictStr | None = None
