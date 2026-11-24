from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class EC2AssociateEnclaveCertificateIamRoleResponse(BaseModel):
    CertificateS3BucketName: StrictStr | None = None
    CertificateS3ObjectKey: StrictStr | None = None
    EncryptionKmsKeyId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
