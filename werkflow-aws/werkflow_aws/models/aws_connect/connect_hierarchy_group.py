from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .connect_hierarchy_path import ConnectHierarchyPath


class ConnectHierarchyGroup(BaseModel):
    Id: StrictStr | None = None
    Arn: StrictStr | None = None
    Name: StrictStr | None = None
    LevelId: StrictStr | None = None
    HierarchyPath: ConnectHierarchyPath | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    LastModifiedRegion: StrictStr | None = None
