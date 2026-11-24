from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .associated_item_bean import AssociatedItemBean
from .changed_value_bean import ChangedValueBean


class AuditRecordBean(BaseModel):
    associatedItems: list[AssociatedItemBean] | None = None
    authorKey: StrictStr | None = None
    category: StrictStr | None = None
    changedValues: list[ChangedValueBean] | None = None
    created: StrictStr | None = None
    description: StrictStr | None = None
    eventSource: StrictStr | None = None
    id: StrictInt | None = None
    objectItem: AssociatedItemBean | None = None
    remoteAddress: StrictStr | None = None
    summary: StrictStr | None = None
