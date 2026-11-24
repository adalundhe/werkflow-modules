from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .document_db_availability_zone import DocumentDBAvailabilityZone


class DocumentDBSubnet(BaseModel):
    SubnetIdentifier: StrictStr | None = None
    SubnetAvailabilityZone: DocumentDBAvailabilityZone | None = None
    SubnetStatus: StrictStr | None = None
