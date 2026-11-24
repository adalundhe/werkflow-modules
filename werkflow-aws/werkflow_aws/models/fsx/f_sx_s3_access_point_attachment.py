from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .f_sx_lifecycle_transition_reason import FSxLifecycleTransitionReason
from .f_sx_s3_access_point import FSxS3AccessPoint
from .f_sx_s3_access_point_ontap_configuration import FSxS3AccessPointOntapConfiguration
from .f_sx_s3_access_point_open_zfs_configuration import FSxS3AccessPointOpenZFSConfiguration


class FSxS3AccessPointAttachment(BaseModel):
    Lifecycle: StrictStr | None = None
    LifecycleTransitionReason: FSxLifecycleTransitionReason | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    Name: StrictStr | None = None
    Type: StrictStr | None = None
    OpenZFSConfiguration: FSxS3AccessPointOpenZFSConfiguration | None = None
    OntapConfiguration: FSxS3AccessPointOntapConfiguration | None = None
    S3AccessPoint: FSxS3AccessPoint | None = None
