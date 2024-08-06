from typing import Any, Dict

from pydantic import AnyHttpUrl, BaseModel, StrictStr


class JiraIssueResponse(BaseModel):
    id: StrictStr
    key: StrictStr
    self: AnyHttpUrl | None = None
    transition: Dict[StrictStr, Any] | None = None
