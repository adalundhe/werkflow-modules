from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .amplify_certificate_settings import AmplifyCertificateSettings
from .amplify_sub_domain_setting import AmplifySubDomainSetting


class AmplifyUpdateDomainAssociationRequest(BaseModel):
    appId: StrictStr
    domainName: StrictStr
    enableAutoSubDomain: StrictBool | None = None
    subDomainSettings: list[AmplifySubDomainSetting] | None = None
    autoSubDomainCreationPatterns: list[StrictStr] | None = None
    autoSubDomainIAMRole: StrictStr | None = None
    certificateSettings: AmplifyCertificateSettings | None = None
