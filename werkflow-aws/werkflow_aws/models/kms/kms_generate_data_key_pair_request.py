from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .kms_recipient_info import KMSRecipientInfo


class KMSGenerateDataKeyPairRequest(BaseModel):
    KeyId: StrictStr
    KeyPairSpec: Literal['RSA_2048', 'RSA_3072', 'RSA_4096', 'ECC_NIST_P256', 'ECC_NIST_P384', 'ECC_NIST_P521', 'ECC_SECG_P256K1', 'SM2', 'ECC_NIST_EDWARDS25519', 'ML_KEM_512', 'ML_KEM_768', 'ML_KEM_1024']
    EncryptionContext: dict[StrictStr, StrictStr] | None = None
    GrantTokens: list[StrictStr] | None = None
    Recipient: KMSRecipientInfo | None = None
    DryRun: StrictBool | None = None
