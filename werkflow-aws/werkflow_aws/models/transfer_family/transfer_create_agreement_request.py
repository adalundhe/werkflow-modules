from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .transfer_custom_directories_type import TransferCustomDirectoriesType
from .transfer_tag import TransferTag


class TransferCreateAgreementRequest(BaseModel):
    ServerId: StrictStr
    LocalProfileId: StrictStr
    PartnerProfileId: StrictStr
    AccessRole: StrictStr
    Description: StrictStr | None = None
    BaseDirectory: StrictStr | None = None
    Status: Literal['ACTIVE', 'INACTIVE'] | None = None
    Tags: list[TransferTag] | None = None
    PreserveFilename: Literal['ENABLED', 'DISABLED'] | None = None
    EnforceMessageSigning: Literal['ENABLED', 'DISABLED'] | None = None
    CustomDirectories: TransferCustomDirectoriesType | None = None
