from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeBuildProjectFileSystemLocation(BaseModel):
    type: StrictStr | None = None
    location: StrictStr | None = None
    mountPoint: StrictStr | None = None
    identifier: StrictStr | None = None
    mountOptions: StrictStr | None = None
