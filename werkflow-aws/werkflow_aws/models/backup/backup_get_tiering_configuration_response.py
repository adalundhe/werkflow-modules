from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .backup_tiering_configuration import BackupTieringConfiguration


class BackupGetTieringConfigurationResponse(BaseModel):
    TieringConfiguration: BackupTieringConfiguration | None = None
    ResponseMetadata: dict[str, Any] | None = None
