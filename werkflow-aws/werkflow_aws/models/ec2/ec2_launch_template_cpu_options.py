from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class EC2LaunchTemplateCpuOptions(BaseModel):
    CoreCount: StrictInt | None = None
    ThreadsPerCore: StrictInt | None = None
    AmdSevSnp: StrictStr | None = None
    NestedVirtualization: StrictStr | None = None
