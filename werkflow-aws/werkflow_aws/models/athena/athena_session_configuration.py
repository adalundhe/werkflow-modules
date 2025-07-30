from pydantic import (
    BaseModel,
    StrictStr,
    StrictInt,
)
from .athena_encryption_configuration import AthenaEncryptionConfiguration


class AthenaSessionConfiguration(BaseModel):
    ExecutionRole: StrictStr
    WorkingDirectory: StrictStr
    IdleTimeoutSeconds: StrictInt
    EncryptionConfiguration: AthenaEncryptionConfiguration