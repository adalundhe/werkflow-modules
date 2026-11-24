from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .transfer_custom_directories_type import TransferCustomDirectoriesType
from .transfer_tag import TransferTag


class TransferDescribedAgreement(BaseModel):
    Arn: StrictStr | None = None
    AgreementId: StrictStr | None = None
    Description: StrictStr | None = None
    Status: StrictStr | None = None
    ServerId: StrictStr | None = None
    LocalProfileId: StrictStr | None = None
    PartnerProfileId: StrictStr | None = None
    BaseDirectory: StrictStr | None = None
    AccessRole: StrictStr | None = None
    Tags: list[TransferTag] | None = None
    PreserveFilename: StrictStr | None = None
    EnforceMessageSigning: StrictStr | None = None
    CustomDirectories: TransferCustomDirectoriesType | None = None
