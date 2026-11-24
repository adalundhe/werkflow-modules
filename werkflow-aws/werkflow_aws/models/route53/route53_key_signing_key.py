from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class Route53KeySigningKey(BaseModel):
    Name: StrictStr | None = None
    KmsArn: StrictStr | None = None
    Flag: StrictInt | None = None
    SigningAlgorithmMnemonic: StrictStr | None = None
    SigningAlgorithmType: StrictInt | None = None
    DigestAlgorithmMnemonic: StrictStr | None = None
    DigestAlgorithmType: StrictInt | None = None
    KeyTag: StrictInt | None = None
    DigestValue: StrictStr | None = None
    PublicKey: StrictStr | None = None
    DSRecord: StrictStr | None = None
    DNSKEYRecord: StrictStr | None = None
    Status: StrictStr | None = None
    StatusMessage: StrictStr | None = None
    CreatedDate: datetime.datetime | StrictStr | None = None
    LastModifiedDate: datetime.datetime | StrictStr | None = None
