from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .transfer_execution_results import TransferExecutionResults
from .transfer_file_location import TransferFileLocation
from .transfer_logging_configuration import TransferLoggingConfiguration
from .transfer_posix_profile import TransferPosixProfile
from .transfer_service_metadata import TransferServiceMetadata


class TransferDescribedExecution(BaseModel):
    ExecutionId: StrictStr | None = None
    InitialFileLocation: TransferFileLocation | None = None
    ServiceMetadata: TransferServiceMetadata | None = None
    ExecutionRole: StrictStr | None = None
    LoggingConfiguration: TransferLoggingConfiguration | None = None
    PosixProfile: TransferPosixProfile | None = None
    Status: StrictStr | None = None
    Results: TransferExecutionResults | None = None
