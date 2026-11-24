from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchLogsLookupTableConfiguration(BaseModel):
    tableName: StrictStr | None = None
    roleArn: StrictStr | None = None
    description: StrictStr | None = None
    kmsKeyId: StrictStr | None = None
    tags: dict[StrictStr, StrictStr] | None = None
