from __future__ import annotations
from typing import BinaryIO, Literal
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictStr


class KMSRecipientInfo(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    KeyEncryptionAlgorithm: Literal['RSAES_OAEP_SHA_256'] | None = None
    AttestationDocument: StrictBytes | BinaryIO | StrictStr | None = None
