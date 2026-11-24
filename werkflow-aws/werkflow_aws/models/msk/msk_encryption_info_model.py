from __future__ import annotations
from pydantic import BaseModel
from .msk_encryption_at_rest_model import MSKEncryptionAtRestModel
from .msk_encryption_in_transit_model import MSKEncryptionInTransitModel


class MSKEncryptionInfoModel(BaseModel):
    EncryptionAtRest: MSKEncryptionAtRestModel | None = None
    EncryptionInTransit: MSKEncryptionInTransitModel | None = None
