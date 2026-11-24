from __future__ import annotations
from typing import Any
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictStr


class KMSSignResponse(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    KeyId: StrictStr | None = None
    Signature: StrictBytes | Any | None = None
    SigningAlgorithm: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
