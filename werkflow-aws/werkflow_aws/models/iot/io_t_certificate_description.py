from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .io_t_certificate_validity import IoTCertificateValidity
from .io_t_transfer_data import IoTTransferData


class IoTCertificateDescription(BaseModel):
    certificateArn: StrictStr | None = None
    certificateId: StrictStr | None = None
    caCertificateId: StrictStr | None = None
    status: StrictStr | None = None
    certificatePem: StrictStr | None = None
    ownedBy: StrictStr | None = None
    previousOwnedBy: StrictStr | None = None
    creationDate: datetime.datetime | StrictStr | None = None
    lastModifiedDate: datetime.datetime | StrictStr | None = None
    customerVersion: StrictInt | None = None
    transferData: IoTTransferData | None = None
    generationId: StrictStr | None = None
    validity: IoTCertificateValidity | None = None
    certificateMode: StrictStr | None = None
