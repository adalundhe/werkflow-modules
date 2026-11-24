from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .f_sx_create_ontap_volume_configuration import FSxCreateOntapVolumeConfiguration
from .f_sx_tag import FSxTag


class FSxCreateVolumeFromBackupRequest(BaseModel):
    BackupId: StrictStr
    Name: StrictStr
    ClientRequestToken: StrictStr | None = None
    OntapConfiguration: FSxCreateOntapVolumeConfiguration | None = None
    Tags: list[FSxTag] | None = None
