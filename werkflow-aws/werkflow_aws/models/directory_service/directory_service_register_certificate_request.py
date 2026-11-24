from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .directory_service_client_cert_auth_settings import DirectoryServiceClientCertAuthSettings


class DirectoryServiceRegisterCertificateRequest(BaseModel):
    DirectoryId: StrictStr
    CertificateData: StrictStr
    Type: Literal['ClientCertAuth', 'ClientLDAPS'] | None = None
    ClientCertAuthSettings: DirectoryServiceClientCertAuthSettings | None = None
