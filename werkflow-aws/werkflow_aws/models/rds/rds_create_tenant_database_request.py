from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .rds_tag_model import RDSTagModel


class RDSCreateTenantDatabaseRequest(BaseModel):
    DBInstanceIdentifier: StrictStr
    TenantDBName: StrictStr
    MasterUsername: StrictStr
    MasterUserPassword: StrictStr | None = None
    CharacterSetName: StrictStr | None = None
    NcharCharacterSetName: StrictStr | None = None
    ManageMasterUserPassword: StrictBool | None = None
    MasterUserSecretKmsKeyId: StrictStr | None = None
    Tags: list[RDSTagModel] | None = None
