from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .efs_destination import EFSDestination


class EFSReplicationConfigurationDescription(BaseModel):
    SourceFileSystemId: StrictStr | None = None
    SourceFileSystemRegion: StrictStr | None = None
    SourceFileSystemArn: StrictStr | None = None
    OriginalSourceFileSystemArn: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    Destinations: list[EFSDestination] | None = None
    SourceFileSystemOwnerId: StrictStr | None = None
