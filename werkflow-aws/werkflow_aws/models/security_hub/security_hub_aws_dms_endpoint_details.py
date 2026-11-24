from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SecurityHubAwsDmsEndpointDetails(BaseModel):
    CertificateArn: StrictStr | None = None
    DatabaseName: StrictStr | None = None
    EndpointArn: StrictStr | None = None
    EndpointIdentifier: StrictStr | None = None
    EndpointType: StrictStr | None = None
    EngineName: StrictStr | None = None
    ExternalId: StrictStr | None = None
    ExtraConnectionAttributes: StrictStr | None = None
    KmsKeyId: StrictStr | None = None
    Port: StrictInt | None = None
    ServerName: StrictStr | None = None
    SslMode: StrictStr | None = None
    Username: StrictStr | None = None
