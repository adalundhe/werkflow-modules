from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .kendra_s3_path import KendraS3Path


class KendraOnPremiseConfiguration(BaseModel):
    HostUrl: StrictStr | None = None
    OrganizationName: StrictStr | None = None
    SslCertificateS3Path: KendraS3Path | None = None
