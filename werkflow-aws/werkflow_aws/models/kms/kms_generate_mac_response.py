from __future__ import annotations
from typing import Any
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictStr


class KMSGenerateMacResponse(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    Mac: StrictBytes | Any | None = None
    MacAlgorithm: StrictStr | None = None
    KeyId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
