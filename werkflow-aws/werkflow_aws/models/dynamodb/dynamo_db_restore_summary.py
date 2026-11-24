from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr


class DynamoDBRestoreSummary(BaseModel):
    SourceBackupArn: StrictStr | None = None
    SourceTableArn: StrictStr | None = None
    RestoreDateTime: datetime.datetime | None = None
    RestoreInProgress: StrictBool | None = None
