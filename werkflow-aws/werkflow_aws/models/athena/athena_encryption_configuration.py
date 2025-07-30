from pydantic import (
    BaseModel,
    StrictStr,
)
from .athena_encryption_option import AthenaEncryptionOption


class AthenaEncryptionConfiguration(BaseModel):
    KmsKey: StrictStr
    EncryptionOption: AthenaEncryptionOption