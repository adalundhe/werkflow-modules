from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class BackupListTieringConfigurationsRequest(BaseModel):
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
