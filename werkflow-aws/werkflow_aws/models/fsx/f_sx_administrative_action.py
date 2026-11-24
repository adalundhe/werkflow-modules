from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .f_sx_administrative_action_failure_details import FSxAdministrativeActionFailureDetails
from .f_sx_file_system import FSxFileSystem
from .f_sx_snapshot import FSxSnapshot
from .f_sx_volume import FSxVolume


class FSxAdministrativeAction(BaseModel):
    AdministrativeActionType: StrictStr | None = None
    ProgressPercent: StrictInt | None = None
    RequestTime: datetime.datetime | StrictStr | None = None
    Status: StrictStr | None = None
    TargetFileSystemValues: FSxFileSystem | None = None
    FailureDetails: FSxAdministrativeActionFailureDetails | None = None
    TargetVolumeValues: FSxVolume | None = None
    TargetSnapshotValues: FSxSnapshot | None = None
    TotalTransferBytes: StrictInt | None = None
    RemainingTransferBytes: StrictInt | None = None
    Message: StrictStr | None = None
