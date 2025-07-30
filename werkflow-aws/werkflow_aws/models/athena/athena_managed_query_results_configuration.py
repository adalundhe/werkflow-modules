from pydantic import (
    BaseModel,
    StrictBool,
)
from .athena_encryption_configuration import AthenaEncryptionConfiguration


class AthenaManagedQueryResultsConfiguration(BaseModel):
    Enabled: StrictBool = True
    EncryptionConfiguration: AthenaEncryptionConfiguration