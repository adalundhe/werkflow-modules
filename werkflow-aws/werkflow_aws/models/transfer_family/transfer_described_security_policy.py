from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class TransferDescribedSecurityPolicy(BaseModel):
    Fips: StrictBool | None = None
    SecurityPolicyName: StrictStr | None = None
    SshCiphers: list[StrictStr] | None = None
    SshKexs: list[StrictStr] | None = None
    SshMacs: list[StrictStr] | None = None
    TlsCiphers: list[StrictStr] | None = None
    SshHostKeyAlgorithms: list[StrictStr] | None = None
    Type: StrictStr | None = None
    Protocols: list[StrictStr] | None = None
