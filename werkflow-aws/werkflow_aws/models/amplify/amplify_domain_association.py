from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .amplify_certificate import AmplifyCertificate
from .amplify_sub_domain import AmplifySubDomain


class AmplifyDomainAssociation(BaseModel):
    domainAssociationArn: StrictStr | None = None
    domainName: StrictStr | None = None
    enableAutoSubDomain: StrictBool | None = None
    autoSubDomainCreationPatterns: list[StrictStr] | None = None
    autoSubDomainIAMRole: StrictStr | None = None
    domainStatus: StrictStr | None = None
    updateStatus: StrictStr | None = None
    statusReason: StrictStr | None = None
    certificateVerificationDNSRecord: StrictStr | None = None
    subDomains: list[AmplifySubDomain] | None = None
    certificate: AmplifyCertificate | None = None
