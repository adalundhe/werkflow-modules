from __future__ import annotations
from typing import BinaryIO, Literal
from pydantic import BaseModel, ConfigDict, StrictBool, StrictBytes, StrictStr


class KMSDecapsulateRequest(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    KeyId: StrictStr
    SharedSecretCiphertextBlob: StrictBytes | BinaryIO | StrictStr
    EncapsulationAlgorithm: Literal['ML_KEM']
    GrantTokens: list[StrictStr] | None = None
    DryRun: StrictBool | None = None
