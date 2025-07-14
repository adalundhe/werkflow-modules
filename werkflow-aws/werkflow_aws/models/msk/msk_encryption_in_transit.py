from pydantic import BaseModel, StrictBool
from .msk_client_broker import MSKClientBroker


class MSKEncryptionInTransit(BaseModel):
    ClientBroker: MSKClientBroker
    InCluster: StrictBool = False