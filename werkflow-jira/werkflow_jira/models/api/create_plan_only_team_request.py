from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class CreatePlanOnlyTeamRequest(BaseModel):
    capacity: StrictFloat | StrictInt | None = None
    issueSourceId: StrictInt | None = None
    memberAccountIds: list[StrictStr] | None = None
    name: StrictStr | None = None
    planningStyle: StrictStr | None = None
    sprintLength: StrictInt | None = None
