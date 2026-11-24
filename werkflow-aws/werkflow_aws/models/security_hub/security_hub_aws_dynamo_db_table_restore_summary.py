from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class SecurityHubAwsDynamoDbTableRestoreSummary(BaseModel):
    SourceBackupArn: StrictStr | None = None
    SourceTableArn: StrictStr | None = None
    RestoreDateTime: StrictStr | None = None
    RestoreInProgress: StrictBool | None = None
