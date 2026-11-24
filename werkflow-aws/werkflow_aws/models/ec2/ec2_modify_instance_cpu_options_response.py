from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class EC2ModifyInstanceCpuOptionsResponse(BaseModel):
    InstanceId: StrictStr | None = None
    CoreCount: StrictInt | None = None
    ThreadsPerCore: StrictInt | None = None
    NestedVirtualization: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
