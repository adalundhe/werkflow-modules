from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2MacHost(BaseModel):
    HostId: StrictStr | None = None
    MacOSLatestSupportedVersions: list[StrictStr] | None = None
