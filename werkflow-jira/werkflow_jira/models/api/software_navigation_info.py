from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class SoftwareNavigationInfo(BaseModel):
    boardId: StrictInt | None = None
    boardName: StrictStr | None = None
    simpleBoard: StrictBool | None = None
    totalBoardsInProject: StrictInt | None = None
