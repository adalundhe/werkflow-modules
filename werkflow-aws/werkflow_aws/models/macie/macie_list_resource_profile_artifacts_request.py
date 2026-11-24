from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MacieListResourceProfileArtifactsRequest(BaseModel):
    resourceArn: StrictStr
    nextToken: StrictStr | None = None
