from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .directory_service_client_cert_auth_settings import DirectoryServiceClientCertAuthSettings


class DirectoryServiceCertificate(BaseModel):
    CertificateId: StrictStr | None = None
    State: StrictStr | None = None
    StateReason: StrictStr | None = None
    CommonName: StrictStr | None = None
    RegisteredDateTime: datetime.datetime | StrictStr | None = None
    ExpiryDateTime: datetime.datetime | StrictStr | None = None
    Type: StrictStr | None = None
    ClientCertAuthSettings: DirectoryServiceClientCertAuthSettings | None = None
