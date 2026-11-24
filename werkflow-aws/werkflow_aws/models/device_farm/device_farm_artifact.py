from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DeviceFarmArtifact(BaseModel):
    arn: StrictStr | None = None
    name: StrictStr | None = None
    type: StrictStr | None = None
    extension: StrictStr | None = None
    url: StrictStr | None = None
