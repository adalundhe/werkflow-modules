from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .transfer_home_directory_map_entry import TransferHomeDirectoryMapEntry
from .transfer_posix_profile import TransferPosixProfile


class TransferDescribedAccess(BaseModel):
    HomeDirectory: StrictStr | None = None
    HomeDirectoryMappings: list[TransferHomeDirectoryMapEntry] | None = None
    HomeDirectoryType: StrictStr | None = None
    Policy: StrictStr | None = None
    PosixProfile: TransferPosixProfile | None = None
    Role: StrictStr | None = None
    ExternalId: StrictStr | None = None
