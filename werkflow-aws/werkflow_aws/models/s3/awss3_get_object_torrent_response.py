from __future__ import annotations
from typing import Any
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictStr


class AWSS3GetObjectTorrentResponse(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    Body: StrictBytes | Any | None = None
    RequestCharged: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
