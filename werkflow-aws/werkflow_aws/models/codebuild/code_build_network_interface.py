from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeBuildNetworkInterface(BaseModel):
    subnetId: StrictStr | None = None
    networkInterfaceId: StrictStr | None = None
