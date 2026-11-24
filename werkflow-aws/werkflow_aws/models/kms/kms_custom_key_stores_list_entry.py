from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .kms_xks_proxy_configuration_type import KMSXksProxyConfigurationType


class KMSCustomKeyStoresListEntry(BaseModel):
    CustomKeyStoreId: StrictStr | None = None
    CustomKeyStoreName: StrictStr | None = None
    CloudHsmClusterId: StrictStr | None = None
    TrustAnchorCertificate: StrictStr | None = None
    ConnectionState: StrictStr | None = None
    ConnectionErrorCode: StrictStr | None = None
    CreationDate: datetime.datetime | StrictStr | None = None
    CustomKeyStoreType: StrictStr | None = None
    XksProxyConfiguration: KMSXksProxyConfigurationType | None = None
