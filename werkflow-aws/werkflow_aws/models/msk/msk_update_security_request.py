from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .msk_client_authentication_model import MSKClientAuthenticationModel
from .msk_encryption_info_model import MSKEncryptionInfoModel


class MSKUpdateSecurityRequest(BaseModel):
    ClusterArn: StrictStr
    CurrentVersion: StrictStr
    ClientAuthentication: MSKClientAuthenticationModel | None = None
    EncryptionInfo: MSKEncryptionInfoModel | None = None
