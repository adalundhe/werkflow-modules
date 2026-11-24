from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .connect_workspace_theme import ConnectWorkspaceTheme


class ConnectWorkspace(BaseModel):
    Visibility: StrictStr | None = None
    Id: StrictStr | None = None
    Name: StrictStr | None = None
    Arn: StrictStr | None = None
    Description: StrictStr | None = None
    Theme: ConnectWorkspaceTheme | None = None
    Title: StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    LastModifiedRegion: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
