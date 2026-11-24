from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SimplifiedHierarchyLevel(BaseModel):
    aboveLevelId: StrictInt | None = None
    belowLevelId: StrictInt | None = None
    externalUuid: StrictStr | None = None
    hierarchyLevelNumber: StrictInt | None = None
    id: StrictInt | None = None
    issueTypeIds: list[StrictInt] | None = None
    level: StrictInt | None = None
    name: StrictStr | None = None
    projectConfigurationId: StrictInt | None = None
