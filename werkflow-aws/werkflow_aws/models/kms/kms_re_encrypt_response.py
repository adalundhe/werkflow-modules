from __future__ import annotations
from typing import Any
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictStr


class KMSReEncryptResponse(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    CiphertextBlob: StrictBytes | Any | None = None
    SourceKeyId: StrictStr | None = None
    KeyId: StrictStr | None = None
    SourceEncryptionAlgorithm: StrictStr | None = None
    DestinationEncryptionAlgorithm: StrictStr | None = None
    SourceKeyMaterialId: StrictStr | None = None
    DestinationKeyMaterialId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
