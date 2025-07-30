from pydantic import (
    BaseModel,
    StrictStr,
)
from .athena_encryption_configuration import AthenaEncryptionConfiguration
from .athena_acl_configuration import AthenaAclConfiguration


class AthenaResultConfigruation(BaseModel):
    OutputLocation: StrictStr
    EncryptionConfiguration: AthenaEncryptionConfiguration
    ExpectedBucketOwner: StrictStr
    AclConfiguration: AthenaAclConfiguration
