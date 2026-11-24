from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class KMSGetParametersForImportRequest(BaseModel):
    KeyId: StrictStr
    WrappingAlgorithm: Literal['RSAES_PKCS1_V1_5', 'RSAES_OAEP_SHA_1', 'RSAES_OAEP_SHA_256', 'RSA_AES_KEY_WRAP_SHA_1', 'RSA_AES_KEY_WRAP_SHA_256', 'SM2PKE']
    WrappingKeySpec: Literal['RSA_2048', 'RSA_3072', 'RSA_4096', 'SM2']
