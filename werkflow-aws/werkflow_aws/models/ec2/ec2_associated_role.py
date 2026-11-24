from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2AssociatedRole(BaseModel):
    AssociatedRoleArn: StrictStr | None = None
    CertificateS3BucketName: StrictStr | None = None
    CertificateS3ObjectKey: StrictStr | None = None
    EncryptionKmsKeyId: StrictStr | None = None
