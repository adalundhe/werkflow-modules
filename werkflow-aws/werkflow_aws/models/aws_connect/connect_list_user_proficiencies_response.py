from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .connect_user_proficiency import ConnectUserProficiency


class ConnectListUserProficienciesResponse(BaseModel):
    NextToken: StrictStr | None = None
    UserProficiencyList: list[ConnectUserProficiency] | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    LastModifiedRegion: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
