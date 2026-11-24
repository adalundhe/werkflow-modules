from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .transfer_home_directory_map_entry import TransferHomeDirectoryMapEntry
from .transfer_posix_profile import TransferPosixProfile
from .transfer_ssh_public_key import TransferSshPublicKey
from .transfer_tag import TransferTag


class TransferDescribedUser(BaseModel):
    Arn: StrictStr | None = None
    HomeDirectory: StrictStr | None = None
    HomeDirectoryMappings: list[TransferHomeDirectoryMapEntry] | None = None
    HomeDirectoryType: StrictStr | None = None
    Policy: StrictStr | None = None
    PosixProfile: TransferPosixProfile | None = None
    Role: StrictStr | None = None
    SshPublicKeys: list[TransferSshPublicKey] | None = None
    Tags: list[TransferTag] | None = None
    UserName: StrictStr | None = None
