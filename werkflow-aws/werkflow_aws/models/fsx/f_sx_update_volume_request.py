from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .f_sx_update_ontap_volume_configuration import FSxUpdateOntapVolumeConfiguration
from .f_sx_update_open_zfs_volume_configuration import FSxUpdateOpenZFSVolumeConfiguration


class FSxUpdateVolumeRequest(BaseModel):
    VolumeId: StrictStr
    ClientRequestToken: StrictStr | None = None
    OntapConfiguration: FSxUpdateOntapVolumeConfiguration | None = None
    Name: StrictStr | None = None
    OpenZFSConfiguration: FSxUpdateOpenZFSVolumeConfiguration | None = None
