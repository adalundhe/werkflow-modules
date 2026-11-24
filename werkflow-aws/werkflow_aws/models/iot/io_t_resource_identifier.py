from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .io_t_issuer_certificate_identifier import IoTIssuerCertificateIdentifier
from .io_t_policy_version_identifier import IoTPolicyVersionIdentifier


class IoTResourceIdentifier(BaseModel):
    deviceCertificateId: StrictStr | None = None
    caCertificateId: StrictStr | None = None
    cognitoIdentityPoolId: StrictStr | None = None
    clientId: StrictStr | None = None
    policyVersionIdentifier: IoTPolicyVersionIdentifier | None = None
    account: StrictStr | None = None
    iamRoleArn: StrictStr | None = None
    roleAliasArn: StrictStr | None = None
    issuerCertificateIdentifier: IoTIssuerCertificateIdentifier | None = None
    deviceCertificateArn: StrictStr | None = None
