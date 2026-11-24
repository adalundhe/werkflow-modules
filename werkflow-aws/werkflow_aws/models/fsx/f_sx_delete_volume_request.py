from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .f_sx_delete_volume_ontap_configuration import FSxDeleteVolumeOntapConfiguration
from .f_sx_delete_volume_open_zfs_configuration import FSxDeleteVolumeOpenZFSConfiguration


class FSxDeleteVolumeRequest(BaseModel):
    VolumeId: StrictStr
    ClientRequestToken: StrictStr | None = None
    OntapConfiguration: FSxDeleteVolumeOntapConfiguration | None = None
    OpenZFSConfiguration: FSxDeleteVolumeOpenZFSConfiguration | None = None
