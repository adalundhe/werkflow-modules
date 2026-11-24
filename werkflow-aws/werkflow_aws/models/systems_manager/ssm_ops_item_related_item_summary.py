from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .ssm_ops_item_identity import SSMOpsItemIdentity


class SSMOpsItemRelatedItemSummary(BaseModel):
    OpsItemId: StrictStr | None = None
    AssociationId: StrictStr | None = None
    ResourceType: StrictStr | None = None
    AssociationType: StrictStr | None = None
    ResourceUri: StrictStr | None = None
    CreatedBy: SSMOpsItemIdentity | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
    LastModifiedBy: SSMOpsItemIdentity | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
