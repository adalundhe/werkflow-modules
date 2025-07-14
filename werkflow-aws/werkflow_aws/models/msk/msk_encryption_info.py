from pydantic import BaseModel
from .msk_encryption_at_rest import MSKEncryptionAtRest
from .msk_encryption_in_transit import MSKEncryptionInTransit


class MSKEncryptionInfo(BaseModel):
    EncryptionAtRest: MSKEncryptionAtRest
    EncryptionInTransit: MSKEncryptionInTransit