from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .f_sx_tag import FSxTag


class FSxCreateClusterPeerRequest(BaseModel):
    FileSystemId: StrictStr
    PeerAddresses: list[StrictStr]
    PassphraseSecretArn: StrictStr
    AllowedSvmMode: Literal['ALL', 'NONE', 'SPECIFIED']
    ClientRequestToken: StrictStr | None = None
    PeerClusterName: StrictStr | None = None
    AllowedSvmIds: list[StrictStr] | None = None
    Tags: list[FSxTag] | None = None
