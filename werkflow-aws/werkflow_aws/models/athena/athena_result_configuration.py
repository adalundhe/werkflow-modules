from pydantic import BaseModel, StrictStr
from .athena_acl_configuration import AthenaAclConfiguration
from .athena_encryption_configuration import AthenaEncryptionConfiguration


class AthenaResultConfiguration(BaseModel):
    OutputLocation: StrictStr | None = None
    EncryptionConfiguration: AthenaEncryptionConfiguration | None = None
    ExpectedBucketOwner: StrictStr | None = None
    AclConfiguration: AthenaAclConfiguration | None = None


AthenaResultConfigruation = AthenaResultConfiguration
