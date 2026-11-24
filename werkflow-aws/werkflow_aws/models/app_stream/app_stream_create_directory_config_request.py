from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .app_stream_certificate_based_auth_properties import AppStreamCertificateBasedAuthProperties
from .app_stream_service_account_credentials import AppStreamServiceAccountCredentials


class AppStreamCreateDirectoryConfigRequest(BaseModel):
    DirectoryName: StrictStr
    OrganizationalUnitDistinguishedNames: list[StrictStr]
    ServiceAccountCredentials: AppStreamServiceAccountCredentials | None = None
    CertificateBasedAuthProperties: AppStreamCertificateBasedAuthProperties | None = None
