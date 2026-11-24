from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class CustomTemplatesProjectDetails(BaseModel):
    accessLevel: StrictStr | None = None
    additionalProperties: dict[StrictStr, StrictStr] | None = None
    assigneeType: StrictStr | None = None
    avatarId: StrictInt | None = None
    categoryId: StrictInt | None = None
    description: StrictStr | None = None
    enableComponents: StrictBool | None = None
    key: StrictStr | None = None
    language: StrictStr | None = None
    leadAccountId: StrictStr | None = None
    name: StrictStr | None = None
    url: StrictStr | None = None
