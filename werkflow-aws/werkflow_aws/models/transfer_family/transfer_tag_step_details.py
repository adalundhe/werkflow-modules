from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .transfer_s3_tag import TransferS3Tag


class TransferTagStepDetails(BaseModel):
    Name: StrictStr | None = None
    Tags: list[TransferS3Tag] | None = None
    SourceFileLocation: StrictStr | None = None
