from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .transfer_input_file_location import TransferInputFileLocation


class TransferCopyStepDetails(BaseModel):
    Name: StrictStr | None = None
    DestinationFileLocation: TransferInputFileLocation | None = None
    OverwriteExisting: StrictStr | None = None
    SourceFileLocation: StrictStr | None = None
