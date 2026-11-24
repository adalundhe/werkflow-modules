from __future__ import annotations
from typing import Any
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictStr


class KMSGenerateDataKeyPairWithoutPlaintextResponse(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    PrivateKeyCiphertextBlob: StrictBytes | Any | None = None
    PublicKey: StrictBytes | Any | None = None
    KeyId: StrictStr | None = None
    KeyPairSpec: StrictStr | None = None
    KeyMaterialId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
