from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .app_stream_certificate_based_auth_properties import AppStreamCertificateBasedAuthProperties
from .app_stream_service_account_credentials import AppStreamServiceAccountCredentials


class AppStreamDirectoryConfig(BaseModel):
    DirectoryName: StrictStr | None = None
    OrganizationalUnitDistinguishedNames: list[StrictStr] | None = None
    ServiceAccountCredentials: AppStreamServiceAccountCredentials | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
    CertificateBasedAuthProperties: AppStreamCertificateBasedAuthProperties | None = None
