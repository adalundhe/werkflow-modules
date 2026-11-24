from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class AddAtlassianTeamRequest(BaseModel):
    capacity: StrictFloat | StrictInt | None = None
    id: StrictStr | None = None
    issueSourceId: StrictInt | None = None
    planningStyle: StrictStr | None = None
    sprintLength: StrictInt | None = None
