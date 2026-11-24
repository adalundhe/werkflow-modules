from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .data_zone_environment_configuration_user_parameter import DataZoneEnvironmentConfigurationUserParameter
from .data_zone_project_membership_assignment import DataZoneProjectMembershipAssignment


class DataZoneCreateProjectRequest(BaseModel):
    domainIdentifier: StrictStr
    name: StrictStr
    description: StrictStr | None = None
    resourceTags: dict[StrictStr, StrictStr] | None = None
    glossaryTerms: list[StrictStr] | None = None
    domainUnitId: StrictStr | None = None
    projectProfileId: StrictStr | None = None
    userParameters: list[DataZoneEnvironmentConfigurationUserParameter] | None = None
    projectCategory: StrictStr | None = None
    projectExecutionRole: StrictStr | None = None
    membershipAssignments: list[DataZoneProjectMembershipAssignment] | None = None
