from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class SSMDescribePatchPropertiesRequest(BaseModel):
    OperatingSystem: Literal['WINDOWS', 'AMAZON_LINUX', 'AMAZON_LINUX_2', 'AMAZON_LINUX_2022', 'UBUNTU', 'REDHAT_ENTERPRISE_LINUX', 'SUSE', 'CENTOS', 'ORACLE_LINUX', 'DEBIAN', 'MACOS', 'RASPBIAN', 'ROCKY_LINUX', 'ALMA_LINUX', 'AMAZON_LINUX_2023']
    Property: Literal['PRODUCT', 'PRODUCT_FAMILY', 'CLASSIFICATION', 'MSRC_SEVERITY', 'PRIORITY', 'SEVERITY']
    PatchSet: Literal['OS', 'APPLICATION'] | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
