from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .rds_tag_model import RDSTagModel


class RDSDBSnapshotTenantDatabase(BaseModel):
    DBSnapshotIdentifier: StrictStr | None = None
    DBInstanceIdentifier: StrictStr | None = None
    DbiResourceId: StrictStr | None = None
    EngineName: StrictStr | None = None
    SnapshotType: StrictStr | None = None
    TenantDatabaseCreateTime: datetime.datetime | StrictStr | None = None
    TenantDBName: StrictStr | None = None
    MasterUsername: StrictStr | None = None
    TenantDatabaseResourceId: StrictStr | None = None
    CharacterSetName: StrictStr | None = None
    DBSnapshotTenantDatabaseARN: StrictStr | None = None
    NcharCharacterSetName: StrictStr | None = None
    TagList: list[RDSTagModel] | None = None
