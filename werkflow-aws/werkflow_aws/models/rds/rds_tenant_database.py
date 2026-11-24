from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr
from .rds_master_user_secret_model import RDSMasterUserSecretModel
from .rds_tag_model import RDSTagModel
from .rds_tenant_database_pending_modified_values import RDSTenantDatabasePendingModifiedValues


class RDSTenantDatabase(BaseModel):
    TenantDatabaseCreateTime: datetime.datetime | StrictStr | None = None
    DBInstanceIdentifier: StrictStr | None = None
    TenantDBName: StrictStr | None = None
    Status: StrictStr | None = None
    MasterUsername: StrictStr | None = None
    DbiResourceId: StrictStr | None = None
    TenantDatabaseResourceId: StrictStr | None = None
    TenantDatabaseARN: StrictStr | None = None
    CharacterSetName: StrictStr | None = None
    NcharCharacterSetName: StrictStr | None = None
    DeletionProtection: StrictBool | None = None
    PendingModifiedValues: RDSTenantDatabasePendingModifiedValues | None = None
    MasterUserSecret: RDSMasterUserSecretModel | None = None
    TagList: list[RDSTagModel] | None = None
