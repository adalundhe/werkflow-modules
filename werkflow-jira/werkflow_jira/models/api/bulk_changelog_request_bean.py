from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class BulkChangelogRequestBean(BaseModel):
    fieldIds: list[StrictStr] | None = None
    issueIdsOrKeys: list[StrictStr] | None = None
    maxResults: StrictInt | None = None
    nextPageToken: StrictStr | None = None
