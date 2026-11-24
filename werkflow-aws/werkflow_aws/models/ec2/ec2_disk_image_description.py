from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class EC2DiskImageDescription(BaseModel):
    Checksum: StrictStr | None = None
    Format: StrictStr | None = None
    ImportManifestUrl: StrictStr | None = None
    Size: StrictInt | None = None
