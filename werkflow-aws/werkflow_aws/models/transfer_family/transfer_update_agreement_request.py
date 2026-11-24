from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .transfer_custom_directories_type import TransferCustomDirectoriesType


class TransferUpdateAgreementRequest(BaseModel):
    AgreementId: StrictStr
    ServerId: StrictStr
    Description: StrictStr | None = None
    Status: Literal['ACTIVE', 'INACTIVE'] | None = None
    LocalProfileId: StrictStr | None = None
    PartnerProfileId: StrictStr | None = None
    BaseDirectory: StrictStr | None = None
    AccessRole: StrictStr | None = None
    PreserveFilename: Literal['ENABLED', 'DISABLED'] | None = None
    EnforceMessageSigning: Literal['ENABLED', 'DISABLED'] | None = None
    CustomDirectories: TransferCustomDirectoriesType | None = None
