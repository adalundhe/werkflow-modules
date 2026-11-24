from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .backup_tiering_configuration_input_for_create import BackupTieringConfigurationInputForCreate


class BackupCreateTieringConfigurationRequest(BaseModel):
    TieringConfiguration: BackupTieringConfigurationInputForCreate
    TieringConfigurationTags: dict[StrictStr, StrictStr] | None = None
    CreatorRequestId: StrictStr | None = None
