from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .managed_blockchain_node_framework_attributes import ManagedBlockchainNodeFrameworkAttributes
from .managed_blockchain_node_log_publishing_configuration import ManagedBlockchainNodeLogPublishingConfiguration


class ManagedBlockchainNode(BaseModel):
    NetworkId: StrictStr | None = None
    MemberId: StrictStr | None = None
    Id: StrictStr | None = None
    InstanceType: StrictStr | None = None
    AvailabilityZone: StrictStr | None = None
    FrameworkAttributes: ManagedBlockchainNodeFrameworkAttributes | None = None
    LogPublishingConfiguration: ManagedBlockchainNodeLogPublishingConfiguration | None = None
    StateDB: StrictStr | None = None
    Status: StrictStr | None = None
    CreationDate: datetime.datetime | StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    Arn: StrictStr | None = None
    KmsKeyArn: StrictStr | None = None
