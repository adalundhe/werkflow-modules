from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .f_sx_create_and_attach_s3_access_point_ontap_configuration import FSxCreateAndAttachS3AccessPointOntapConfiguration
from .f_sx_create_and_attach_s3_access_point_open_zfs_configuration import FSxCreateAndAttachS3AccessPointOpenZFSConfiguration
from .f_sx_create_and_attach_s3_access_point_s3_configuration import FSxCreateAndAttachS3AccessPointS3Configuration


class FSxCreateAndAttachS3AccessPointRequest(BaseModel):
    Name: StrictStr
    Type: Literal['OPENZFS', 'ONTAP']
    ClientRequestToken: StrictStr | None = None
    OpenZFSConfiguration: FSxCreateAndAttachS3AccessPointOpenZFSConfiguration | None = None
    OntapConfiguration: FSxCreateAndAttachS3AccessPointOntapConfiguration | None = None
    S3AccessPoint: FSxCreateAndAttachS3AccessPointS3Configuration | None = None
