from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .amplify_certificate_settings import AmplifyCertificateSettings
from .amplify_sub_domain_setting import AmplifySubDomainSetting


class AmplifyCreateDomainAssociationRequest(BaseModel):
    appId: StrictStr
    domainName: StrictStr
    subDomainSettings: list[AmplifySubDomainSetting]
    enableAutoSubDomain: StrictBool | None = None
    autoSubDomainCreationPatterns: list[StrictStr] | None = None
    autoSubDomainIAMRole: StrictStr | None = None
    certificateSettings: AmplifyCertificateSettings | None = None
