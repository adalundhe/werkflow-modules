from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_certificate_authentication import EC2CertificateAuthentication
from .ec2_directory_service_authentication import EC2DirectoryServiceAuthentication
from .ec2_federated_authentication import EC2FederatedAuthentication


class EC2ClientVpnAuthentication(BaseModel):
    Type: StrictStr | None = None
    ActiveDirectory: EC2DirectoryServiceAuthentication | None = None
    MutualAuthentication: EC2CertificateAuthentication | None = None
    FederatedAuthentication: EC2FederatedAuthentication | None = None
