from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .ec2_certificate_authentication_request import EC2CertificateAuthenticationRequest
from .ec2_directory_service_authentication_request import EC2DirectoryServiceAuthenticationRequest
from .ec2_federated_authentication_request import EC2FederatedAuthenticationRequest


class EC2ClientVpnAuthenticationRequest(BaseModel):
    Type: Literal['certificate-authentication', 'directory-service-authentication', 'federated-authentication'] | None = None
    ActiveDirectory: EC2DirectoryServiceAuthenticationRequest | None = None
    MutualAuthentication: EC2CertificateAuthenticationRequest | None = None
    FederatedAuthentication: EC2FederatedAuthenticationRequest | None = None
