from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class RedshiftRestoreTableFromClusterSnapshotRequest(BaseModel):
    ClusterIdentifier: StrictStr
    SnapshotIdentifier: StrictStr
    SourceDatabaseName: StrictStr
    SourceTableName: StrictStr
    NewTableName: StrictStr
    SourceSchemaName: StrictStr | None = None
    TargetDatabaseName: StrictStr | None = None
    TargetSchemaName: StrictStr | None = None
    EnableCaseSensitiveIdentifier: StrictBool | None = None
