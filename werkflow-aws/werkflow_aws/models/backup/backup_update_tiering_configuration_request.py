from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .backup_tiering_configuration_input_for_update import BackupTieringConfigurationInputForUpdate


class BackupUpdateTieringConfigurationRequest(BaseModel):
    TieringConfigurationName: StrictStr
    TieringConfiguration: BackupTieringConfigurationInputForUpdate
