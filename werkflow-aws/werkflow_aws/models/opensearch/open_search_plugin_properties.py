from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class OpenSearchPluginProperties(BaseModel):
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    Version: StrictStr | None = None
    ClassName: StrictStr | None = None
    UncompressedSizeInBytes: StrictInt | None = None
