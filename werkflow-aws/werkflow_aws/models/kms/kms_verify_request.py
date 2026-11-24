from __future__ import annotations
from typing import BinaryIO, Literal
from pydantic import BaseModel, ConfigDict, StrictBool, StrictBytes, StrictStr


class KMSVerifyRequest(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    KeyId: StrictStr
    Message: StrictBytes | BinaryIO | StrictStr
    Signature: StrictBytes | BinaryIO | StrictStr
    SigningAlgorithm: Literal['RSASSA_PSS_SHA_256', 'RSASSA_PSS_SHA_384', 'RSASSA_PSS_SHA_512', 'RSASSA_PKCS1_V1_5_SHA_256', 'RSASSA_PKCS1_V1_5_SHA_384', 'RSASSA_PKCS1_V1_5_SHA_512', 'ECDSA_SHA_256', 'ECDSA_SHA_384', 'ECDSA_SHA_512', 'SM2DSA', 'ML_DSA_SHAKE_256', 'ED25519_SHA_512', 'ED25519_PH_SHA_512']
    MessageType: Literal['RAW', 'DIGEST', 'EXTERNAL_MU'] | None = None
    GrantTokens: list[StrictStr] | None = None
    DryRun: StrictBool | None = None
