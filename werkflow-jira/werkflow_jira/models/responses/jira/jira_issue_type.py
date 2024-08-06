from typing import Dict, Literal

from pydantic import AnyHttpUrl, BaseModel, StrictBool, StrictInt, StrictStr


class JiraIssueTypeScope(BaseModel):
    project: Dict[Literal["id"], StrictStr]
    type: Literal["PROJECT"] = "PROJECT"


class JiraIssueType(BaseModel):
    avatarId: StrictInt
    description: StrictStr
    entityId: StrictStr | None = None
    hierarchyLevel: StrictInt
    iconUrl: AnyHttpUrl | None = None
    id: StrictStr
    name: StrictStr
    scope: JiraIssueTypeScope | None = None
    self: AnyHttpUrl | None = None
    subtask: StrictBool
