from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class QuickSightAssetBundleImportJobRefreshScheduleOverrideParameters(BaseModel):
    DataSetId: StrictStr | None = None
    ScheduleId: StrictStr | None = None
    StartAfterDateTime: datetime.datetime | StrictStr | None = None
