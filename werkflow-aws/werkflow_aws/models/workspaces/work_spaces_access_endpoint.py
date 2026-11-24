from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WorkSpacesAccessEndpoint(BaseModel):
    AccessEndpointType: StrictStr | None = None
    VpcEndpointId: StrictStr | None = None
