from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr


class DynamoDBRestoreSummaryModel(BaseModel):
    SourceBackupArn: StrictStr | None = None
    SourceTableArn: StrictStr | None = None
    RestoreDateTime: datetime.datetime | StrictStr | None = None
    RestoreInProgress: StrictBool | None = None
