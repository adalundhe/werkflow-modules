from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CodeArtifactAssetSummary(BaseModel):
    name: StrictStr | None = None
    size: StrictInt | None = None
    hashes: dict[StrictStr, StrictStr] | None = None
