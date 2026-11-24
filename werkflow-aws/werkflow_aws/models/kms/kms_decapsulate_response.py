from __future__ import annotations
from typing import Any
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictStr


class KMSDecapsulateResponse(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    KeyId: StrictStr | None = None
    SharedSecret: StrictBytes | Any | None = None
    EncapsulationAlgorithm: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
