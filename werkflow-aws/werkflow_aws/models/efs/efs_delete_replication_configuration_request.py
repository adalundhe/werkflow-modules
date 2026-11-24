from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class EFSDeleteReplicationConfigurationRequest(BaseModel):
    SourceFileSystemId: StrictStr
    DeletionMode: Literal['ALL_CONFIGURATIONS', 'LOCAL_CONFIGURATION_ONLY'] | None = None
