from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .athena_acl_configuration_model import AthenaAclConfigurationModel
from .athena_encryption_configuration_model import AthenaEncryptionConfigurationModel


class AthenaResultConfigurationUpdates(BaseModel):
    OutputLocation: StrictStr | None = None
    RemoveOutputLocation: StrictBool | None = None
    EncryptionConfiguration: AthenaEncryptionConfigurationModel | None = None
    RemoveEncryptionConfiguration: StrictBool | None = None
    ExpectedBucketOwner: StrictStr | None = None
    RemoveExpectedBucketOwner: StrictBool | None = None
    AclConfiguration: AthenaAclConfigurationModel | None = None
    RemoveAclConfiguration: StrictBool | None = None
