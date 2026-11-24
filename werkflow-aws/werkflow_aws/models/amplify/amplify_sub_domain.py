from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .amplify_sub_domain_setting import AmplifySubDomainSetting


class AmplifySubDomain(BaseModel):
    subDomainSetting: AmplifySubDomainSetting | None = None
    verified: StrictBool | None = None
    dnsRecord: StrictStr | None = None
