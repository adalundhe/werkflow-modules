from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .efs_destination_to_create import EFSDestinationToCreate


class EFSCreateReplicationConfigurationRequest(BaseModel):
    SourceFileSystemId: StrictStr
    Destinations: list[EFSDestinationToCreate]
