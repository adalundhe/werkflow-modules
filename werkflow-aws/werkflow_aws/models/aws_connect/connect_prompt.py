from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class ConnectPrompt(BaseModel):
    PromptARN: StrictStr | None = None
    PromptId: StrictStr | None = None
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    LastModifiedRegion: StrictStr | None = None
