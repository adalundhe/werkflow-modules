from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .athena_acl_configuration_model import AthenaAclConfigurationModel
from .athena_encryption_configuration_model import AthenaEncryptionConfigurationModel


class AthenaResultConfigurationModel(BaseModel):
    OutputLocation: StrictStr | None = None
    EncryptionConfiguration: AthenaEncryptionConfigurationModel | None = None
    ExpectedBucketOwner: StrictStr | None = None
    AclConfiguration: AthenaAclConfigurationModel | None = None
