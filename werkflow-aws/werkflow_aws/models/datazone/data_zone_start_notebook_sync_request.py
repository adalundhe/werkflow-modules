from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .data_zone_git_metadata import DataZoneGitMetadata
from .data_zone_source_location import DataZoneSourceLocation


class DataZoneStartNotebookSyncRequest(BaseModel):
    domainIdentifier: StrictStr
    owningProjectIdentifier: StrictStr
    sourceLocation: DataZoneSourceLocation
    gitMetadata: DataZoneGitMetadata | None = None
    notebookId: StrictStr | None = None
    name: StrictStr | None = None
    description: StrictStr | None = None
    clientToken: StrictStr | None = None
