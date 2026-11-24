from __future__ import annotations
from typing import Any
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictStr


class KMSDecryptResponse(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    KeyId: StrictStr | None = None
    Plaintext: StrictBytes | Any | None = None
    EncryptionAlgorithm: StrictStr | None = None
    CiphertextForRecipient: StrictBytes | Any | None = None
    KeyMaterialId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
