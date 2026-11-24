from __future__ import annotations
from pydantic import BaseModel
from .data_zone_subscribed_group import DataZoneSubscribedGroup
from .data_zone_subscribed_iam_principal import DataZoneSubscribedIamPrincipal
from .data_zone_subscribed_project import DataZoneSubscribedProject
from .data_zone_subscribed_user import DataZoneSubscribedUser


class DataZoneSubscribedPrincipal(BaseModel):
    project: DataZoneSubscribedProject | None = None
    user: DataZoneSubscribedUser | None = None
    group: DataZoneSubscribedGroup | None = None
    iam: DataZoneSubscribedIamPrincipal | None = None
