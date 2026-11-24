from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class EKSAccessEntry(BaseModel):
    clusterName: StrictStr | None = None
    principalArn: StrictStr | None = None
    kubernetesGroups: list[StrictStr] | None = None
    accessEntryArn: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    modifiedAt: datetime.datetime | StrictStr | None = None
    tags: dict[StrictStr, StrictStr] | None = None
    username: StrictStr | None = None
    type: StrictStr | None = None
