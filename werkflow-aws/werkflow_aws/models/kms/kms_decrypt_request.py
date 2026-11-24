from __future__ import annotations
from typing import BinaryIO, Literal
from pydantic import BaseModel, ConfigDict, StrictBool, StrictBytes, StrictStr
from .kms_recipient_info import KMSRecipientInfo


class KMSDecryptRequest(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    CiphertextBlob: StrictBytes | BinaryIO | StrictStr | None = None
    EncryptionContext: dict[StrictStr, StrictStr] | None = None
    GrantTokens: list[StrictStr] | None = None
    KeyId: StrictStr | None = None
    EncryptionAlgorithm: Literal['SYMMETRIC_DEFAULT', 'RSAES_OAEP_SHA_1', 'RSAES_OAEP_SHA_256', 'SM2PKE'] | None = None
    Recipient: KMSRecipientInfo | None = None
    DryRun: StrictBool | None = None
    DryRunModifiers: list[Literal['IGNORE_CIPHERTEXT']] | None = None
