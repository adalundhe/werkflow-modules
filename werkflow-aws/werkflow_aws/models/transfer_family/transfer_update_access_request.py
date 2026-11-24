from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .transfer_home_directory_map_entry import TransferHomeDirectoryMapEntry
from .transfer_posix_profile import TransferPosixProfile


class TransferUpdateAccessRequest(BaseModel):
    ServerId: StrictStr
    ExternalId: StrictStr
    HomeDirectory: StrictStr | None = None
    HomeDirectoryType: Literal['PATH', 'LOGICAL'] | None = None
    HomeDirectoryMappings: list[TransferHomeDirectoryMapEntry] | None = None
    Policy: StrictStr | None = None
    PosixProfile: TransferPosixProfile | None = None
    Role: StrictStr | None = None
