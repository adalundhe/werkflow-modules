from __future__ import annotations
from typing import BinaryIO, Literal
from pydantic import BaseModel, ConfigDict, StrictBool, StrictBytes, StrictStr
from .kms_recipient_info import KMSRecipientInfo


class KMSDeriveSharedSecretRequest(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    KeyId: StrictStr
    KeyAgreementAlgorithm: Literal['ECDH']
    PublicKey: StrictBytes | BinaryIO | StrictStr
    GrantTokens: list[StrictStr] | None = None
    DryRun: StrictBool | None = None
    Recipient: KMSRecipientInfo | None = None
