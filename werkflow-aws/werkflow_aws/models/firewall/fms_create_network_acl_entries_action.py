from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .fms_action_target import FMSActionTarget
from .fms_entry_description import FMSEntryDescription


class FMSCreateNetworkAclEntriesAction(BaseModel):
    Description: StrictStr | None = None
    NetworkAclId: FMSActionTarget | None = None
    NetworkAclEntriesToBeCreated: list[FMSEntryDescription] | None = None
    FMSCanRemediate: StrictBool | None = None
