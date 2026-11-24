from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .backup_tiering_configurations_list_member import BackupTieringConfigurationsListMember


class BackupListTieringConfigurationsResponse(BaseModel):
    TieringConfigurations: list[BackupTieringConfigurationsListMember] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
