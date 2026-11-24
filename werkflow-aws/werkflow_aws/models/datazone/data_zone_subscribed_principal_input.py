from __future__ import annotations
from pydantic import BaseModel
from .data_zone_subscribed_group_input import DataZoneSubscribedGroupInput
from .data_zone_subscribed_iam_principal_input import DataZoneSubscribedIamPrincipalInput
from .data_zone_subscribed_project_input import DataZoneSubscribedProjectInput
from .data_zone_subscribed_user_input import DataZoneSubscribedUserInput


class DataZoneSubscribedPrincipalInput(BaseModel):
    project: DataZoneSubscribedProjectInput | None = None
    user: DataZoneSubscribedUserInput | None = None
    group: DataZoneSubscribedGroupInput | None = None
    iam: DataZoneSubscribedIamPrincipalInput | None = None
