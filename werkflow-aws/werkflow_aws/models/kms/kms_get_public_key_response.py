from __future__ import annotations
from typing import Any
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictStr


class KMSGetPublicKeyResponse(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    KeyId: StrictStr | None = None
    PublicKey: StrictBytes | Any | None = None
    CustomerMasterKeySpec: StrictStr | None = None
    KeySpec: StrictStr | None = None
    KeyUsage: StrictStr | None = None
    EncryptionAlgorithms: list[StrictStr] | None = None
    SigningAlgorithms: list[StrictStr] | None = None
    KeyAgreementAlgorithms: list[StrictStr] | None = None
    EncapsulationAlgorithms: list[StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
