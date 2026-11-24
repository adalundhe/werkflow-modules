from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class ProjectLandingPageInfo(BaseModel):
    attributes: dict[StrictStr, StrictStr] | None = None
    boardId: StrictInt | None = None
    boardName: StrictStr | None = None
    projectKey: StrictStr | None = None
    projectType: StrictStr | None = None
    queueCategory: StrictStr | None = None
    queueId: StrictInt | None = None
    queueName: StrictStr | None = None
    simpleBoard: StrictBool | None = None
    simplified: StrictBool | None = None
    url: StrictStr | None = None
