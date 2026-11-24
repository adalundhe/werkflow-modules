from __future__ import annotations
from typing import Any
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictStr


class KMSGenerateDataKeyResponse(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    CiphertextBlob: StrictBytes | Any | None = None
    Plaintext: StrictBytes | Any | None = None
    KeyId: StrictStr | None = None
    CiphertextForRecipient: StrictBytes | Any | None = None
    KeyMaterialId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
