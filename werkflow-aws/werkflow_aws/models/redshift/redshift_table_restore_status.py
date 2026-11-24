from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class RedshiftTableRestoreStatus(BaseModel):
    TableRestoreRequestId: StrictStr | None = None
    Status: StrictStr | None = None
    Message: StrictStr | None = None
    RequestTime: datetime.datetime | StrictStr | None = None
    ProgressInMegaBytes: StrictInt | None = None
    TotalDataInMegaBytes: StrictInt | None = None
    ClusterIdentifier: StrictStr | None = None
    SnapshotIdentifier: StrictStr | None = None
    SourceDatabaseName: StrictStr | None = None
    SourceSchemaName: StrictStr | None = None
    SourceTableName: StrictStr | None = None
    TargetDatabaseName: StrictStr | None = None
    TargetSchemaName: StrictStr | None = None
    NewTableName: StrictStr | None = None
