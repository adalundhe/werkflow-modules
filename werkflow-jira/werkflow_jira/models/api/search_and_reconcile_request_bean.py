from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class SearchAndReconcileRequestBean(BaseModel):
    expand: StrictStr | None = None
    fields: list[StrictStr] | None = None
    fieldsByKeys: StrictBool | None = None
    includeArchivedProjects: StrictBool | None = None
    jql: StrictStr | None = None
    maxResults: StrictInt | None = None
    nextPageToken: StrictStr | None = None
    properties: list[StrictStr] | None = None
    reconcileIssues: list[StrictInt] | None = None
