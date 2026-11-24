from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .f_sx_create_ontap_volume_configuration import FSxCreateOntapVolumeConfiguration
from .f_sx_create_open_zfs_volume_configuration import FSxCreateOpenZFSVolumeConfiguration
from .f_sx_tag import FSxTag


class FSxCreateVolumeRequest(BaseModel):
    VolumeType: Literal['ONTAP', 'OPENZFS']
    Name: StrictStr
    ClientRequestToken: StrictStr | None = None
    OntapConfiguration: FSxCreateOntapVolumeConfiguration | None = None
    Tags: list[FSxTag] | None = None
    OpenZFSConfiguration: FSxCreateOpenZFSVolumeConfiguration | None = None
