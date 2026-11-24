from __future__ import annotations
from typing import BinaryIO, Literal
from pydantic import BaseModel, ConfigDict, StrictBool, StrictBytes, StrictStr


class KMSReEncryptRequest(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    DestinationKeyId: StrictStr
    CiphertextBlob: StrictBytes | BinaryIO | StrictStr | None = None
    SourceEncryptionContext: dict[StrictStr, StrictStr] | None = None
    SourceKeyId: StrictStr | None = None
    DestinationEncryptionContext: dict[StrictStr, StrictStr] | None = None
    SourceEncryptionAlgorithm: Literal['SYMMETRIC_DEFAULT', 'RSAES_OAEP_SHA_1', 'RSAES_OAEP_SHA_256', 'SM2PKE'] | None = None
    DestinationEncryptionAlgorithm: Literal['SYMMETRIC_DEFAULT', 'RSAES_OAEP_SHA_1', 'RSAES_OAEP_SHA_256', 'SM2PKE'] | None = None
    GrantTokens: list[StrictStr] | None = None
    DryRun: StrictBool | None = None
    DryRunModifiers: list[Literal['IGNORE_CIPHERTEXT']] | None = None
