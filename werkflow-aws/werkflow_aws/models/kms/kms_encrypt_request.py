from __future__ import annotations
from typing import BinaryIO, Literal
from pydantic import BaseModel, ConfigDict, StrictBool, StrictBytes, StrictStr


class KMSEncryptRequest(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    KeyId: StrictStr
    Plaintext: StrictBytes | BinaryIO | StrictStr
    EncryptionContext: dict[StrictStr, StrictStr] | None = None
    GrantTokens: list[StrictStr] | None = None
    EncryptionAlgorithm: Literal['SYMMETRIC_DEFAULT', 'RSAES_OAEP_SHA_1', 'RSAES_OAEP_SHA_256', 'SM2PKE'] | None = None
    DryRun: StrictBool | None = None
