from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr


class DMSTableStatistics(BaseModel):
    SchemaName: StrictStr | None = None
    TableName: StrictStr | None = None
    Inserts: StrictInt | None = None
    Deletes: StrictInt | None = None
    Updates: StrictInt | None = None
    Ddls: StrictInt | None = None
    AppliedInserts: StrictInt | None = None
    AppliedDeletes: StrictInt | None = None
    AppliedUpdates: StrictInt | None = None
    AppliedDdls: StrictInt | None = None
    FullLoadRows: StrictInt | None = None
    FullLoadCondtnlChkFailedRows: StrictInt | None = None
    FullLoadErrorRows: StrictInt | None = None
    FullLoadStartTime: datetime.datetime | StrictStr | None = None
    FullLoadEndTime: datetime.datetime | StrictStr | None = None
    FullLoadReloaded: StrictBool | None = None
    LastUpdateTime: datetime.datetime | StrictStr | None = None
    TableState: StrictStr | None = None
    ValidationPendingRecords: StrictInt | None = None
    ValidationFailedRecords: StrictInt | None = None
    ValidationSuspendedRecords: StrictInt | None = None
    ValidationState: StrictStr | None = None
    ValidationStateDetails: StrictStr | None = None
    ResyncState: StrictStr | None = None
    ResyncRowsAttempted: StrictInt | None = None
    ResyncRowsSucceeded: StrictInt | None = None
    ResyncRowsFailed: StrictInt | None = None
    ResyncProgress: StrictFloat | StrictInt | None = None
