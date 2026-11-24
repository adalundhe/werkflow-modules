from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .f_sx_ontap_file_system_identity import FSxOntapFileSystemIdentity


class FSxCreateAndAttachS3AccessPointOntapConfiguration(BaseModel):
    VolumeId: StrictStr
    FileSystemIdentity: FSxOntapFileSystemIdentity
