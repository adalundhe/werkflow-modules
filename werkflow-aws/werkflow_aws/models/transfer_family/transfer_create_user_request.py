from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .transfer_home_directory_map_entry import TransferHomeDirectoryMapEntry
from .transfer_posix_profile import TransferPosixProfile
from .transfer_tag import TransferTag


class TransferCreateUserRequest(BaseModel):
    Role: StrictStr
    ServerId: StrictStr
    UserName: StrictStr
    HomeDirectory: StrictStr | None = None
    HomeDirectoryType: Literal['PATH', 'LOGICAL'] | None = None
    HomeDirectoryMappings: list[TransferHomeDirectoryMapEntry] | None = None
    Policy: StrictStr | None = None
    PosixProfile: TransferPosixProfile | None = None
    SshPublicKeyBody: StrictStr | None = None
    Tags: list[TransferTag] | None = None
