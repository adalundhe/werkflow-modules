from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .f_sx_lifecycle_transition_reason import FSxLifecycleTransitionReason
from .f_sx_tag import FSxTag


class FSxStorageVirtualMachinePeer(BaseModel):
    ResourceARN: StrictStr | None = None
    StorageVirtualMachinePeerId: StrictStr | None = None
    StorageVirtualMachineId: StrictStr | None = None
    FileSystemId: StrictStr | None = None
    Lifecycle: StrictStr | None = None
    LifecycleTransitionReason: FSxLifecycleTransitionReason | None = None
    Tags: list[FSxTag] | None = None
    PeerSvmName: StrictStr | None = None
    PeerSvmAlias: StrictStr | None = None
    PeerClusterName: StrictStr | None = None
    Applications: list[StrictStr] | None = None
    State: StrictStr | None = None
    UUID: StrictStr | None = None
