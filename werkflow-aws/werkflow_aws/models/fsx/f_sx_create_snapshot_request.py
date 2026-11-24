from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .f_sx_create_ontap_snapshot_configuration import FSxCreateOntapSnapshotConfiguration
from .f_sx_tag import FSxTag


class FSxCreateSnapshotRequest(BaseModel):
    Name: StrictStr
    VolumeId: StrictStr
    ClientRequestToken: StrictStr | None = None
    Tags: list[FSxTag] | None = None
    OntapConfiguration: FSxCreateOntapSnapshotConfiguration | None = None
