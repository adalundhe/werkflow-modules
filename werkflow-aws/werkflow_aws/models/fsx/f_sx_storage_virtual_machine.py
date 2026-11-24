from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .f_sx_lifecycle_transition_reason import FSxLifecycleTransitionReason
from .f_sx_svm_active_directory_configuration import FSxSvmActiveDirectoryConfiguration
from .f_sx_svm_endpoints import FSxSvmEndpoints
from .f_sx_tag import FSxTag


class FSxStorageVirtualMachine(BaseModel):
    ActiveDirectoryConfiguration: FSxSvmActiveDirectoryConfiguration | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    Endpoints: FSxSvmEndpoints | None = None
    FileSystemId: StrictStr | None = None
    Lifecycle: StrictStr | None = None
    Name: StrictStr | None = None
    ResourceARN: StrictStr | None = None
    StorageVirtualMachineId: StrictStr | None = None
    Subtype: StrictStr | None = None
    UUID: StrictStr | None = None
    Tags: list[FSxTag] | None = None
    LifecycleTransitionReason: FSxLifecycleTransitionReason | None = None
    RootVolumeSecurityStyle: StrictStr | None = None
