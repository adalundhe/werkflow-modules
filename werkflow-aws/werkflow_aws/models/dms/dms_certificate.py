from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictInt, StrictStr


class DMSCertificate(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    CertificateIdentifier: StrictStr | None = None
    CertificateCreationDate: datetime.datetime | StrictStr | None = None
    CertificatePem: StrictStr | None = None
    CertificateWallet: StrictBytes | Any | None = None
    CertificateArn: StrictStr | None = None
    CertificateOwner: StrictStr | None = None
    ValidFromDate: datetime.datetime | StrictStr | None = None
    ValidToDate: datetime.datetime | StrictStr | None = None
    SigningAlgorithm: StrictStr | None = None
    KeyLength: StrictInt | None = None
    KmsKeyId: StrictStr | None = None
