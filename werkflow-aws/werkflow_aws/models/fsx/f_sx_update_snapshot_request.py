from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .f_sx_update_ontap_snapshot_configuration import FSxUpdateOntapSnapshotConfiguration


class FSxUpdateSnapshotRequest(BaseModel):
    SnapshotId: StrictStr
    ClientRequestToken: StrictStr | None = None
    Name: StrictStr | None = None
    OntapConfiguration: FSxUpdateOntapSnapshotConfiguration | None = None
