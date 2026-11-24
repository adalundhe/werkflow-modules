from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_role_group_assignment import SageMakerRoleGroupAssignment


class SageMakerPartnerAppConfig(BaseModel):
    AdminUsers: list[StrictStr] | None = None
    Arguments: dict[StrictStr, StrictStr] | None = None
    AssignedGroupPatterns: list[StrictStr] | None = None
    RoleGroupAssignments: list[SageMakerRoleGroupAssignment] | None = None
