from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AssociatedItemBean(BaseModel):
    id: StrictStr | None = None
    name: StrictStr | None = None
    parentId: StrictStr | None = None
    parentName: StrictStr | None = None
    typeName: StrictStr | None = None
