from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .version_usage_in_custom_field import VersionUsageInCustomField


class VersionIssueCounts(BaseModel):
    customFieldUsage: list[VersionUsageInCustomField] | None = None
    issueCountWithCustomFieldsShowingVersion: StrictInt | None = None
    issuesAffectedCount: StrictInt | None = None
    issuesFixedCount: StrictInt | None = None
    self: StrictStr | None = None
