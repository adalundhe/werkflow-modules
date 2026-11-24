from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_client_certificate_revocation_list_status import EC2ClientCertificateRevocationListStatus


class EC2ExportClientVpnClientCertificateRevocationListResponse(BaseModel):
    CertificateRevocationList: StrictStr | None = None
    Status: EC2ClientCertificateRevocationListStatus | None = None
    ResponseMetadata: dict[str, Any] | None = None
