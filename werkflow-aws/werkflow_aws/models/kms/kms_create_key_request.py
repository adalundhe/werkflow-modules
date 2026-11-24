from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .kms_tag import KMSTag


class KMSCreateKeyRequest(BaseModel):
    Policy: StrictStr | None = None
    Description: StrictStr | None = None
    KeyUsage: Literal['SIGN_VERIFY', 'ENCRYPT_DECRYPT', 'GENERATE_VERIFY_MAC', 'KEY_AGREEMENT', 'ENCAPSULATE_DECAPSULATE'] | None = None
    CustomerMasterKeySpec: Literal['RSA_2048', 'RSA_3072', 'RSA_4096', 'ECC_NIST_P256', 'ECC_NIST_P384', 'ECC_NIST_P521', 'ECC_SECG_P256K1', 'SYMMETRIC_DEFAULT', 'HMAC_224', 'HMAC_256', 'HMAC_384', 'HMAC_512', 'SM2'] | None = None
    KeySpec: Literal['RSA_2048', 'RSA_3072', 'RSA_4096', 'ECC_NIST_P256', 'ECC_NIST_P384', 'ECC_NIST_P521', 'ECC_SECG_P256K1', 'SYMMETRIC_DEFAULT', 'HMAC_224', 'HMAC_256', 'HMAC_384', 'HMAC_512', 'SM2', 'ML_DSA_44', 'ML_DSA_65', 'ML_DSA_87', 'ECC_NIST_EDWARDS25519', 'ML_KEM_512', 'ML_KEM_768', 'ML_KEM_1024'] | None = None
    Origin: Literal['AWS_KMS', 'EXTERNAL', 'AWS_CLOUDHSM', 'EXTERNAL_KEY_STORE'] | None = None
    CustomKeyStoreId: StrictStr | None = None
    BypassPolicyLockoutSafetyCheck: StrictBool | None = None
    Tags: list[KMSTag] | None = None
    MultiRegion: StrictBool | None = None
    XksKeyId: StrictStr | None = None
