from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .transfer_file_location import TransferFileLocation
from .transfer_service_metadata import TransferServiceMetadata


class TransferListedExecution(BaseModel):
    ExecutionId: StrictStr | None = None
    InitialFileLocation: TransferFileLocation | None = None
    ServiceMetadata: TransferServiceMetadata | None = None
    Status: StrictStr | None = None
