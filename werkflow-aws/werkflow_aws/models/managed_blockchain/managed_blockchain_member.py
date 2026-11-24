from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .managed_blockchain_member_framework_attributes import ManagedBlockchainMemberFrameworkAttributes
from .managed_blockchain_member_log_publishing_configuration import ManagedBlockchainMemberLogPublishingConfiguration


class ManagedBlockchainMember(BaseModel):
    NetworkId: StrictStr | None = None
    Id: StrictStr | None = None
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    FrameworkAttributes: ManagedBlockchainMemberFrameworkAttributes | None = None
    LogPublishingConfiguration: ManagedBlockchainMemberLogPublishingConfiguration | None = None
    Status: StrictStr | None = None
    CreationDate: datetime.datetime | StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    Arn: StrictStr | None = None
    KmsKeyArn: StrictStr | None = None
