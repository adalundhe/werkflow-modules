from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .kendra_capacity_units_configuration import KendraCapacityUnitsConfiguration
from .kendra_document_metadata_configuration import KendraDocumentMetadataConfiguration
from .kendra_user_group_resolution_configuration import KendraUserGroupResolutionConfiguration
from .kendra_user_token_configuration import KendraUserTokenConfiguration


class KendraUpdateIndexRequest(BaseModel):
    Id: StrictStr
    Name: StrictStr | None = None
    RoleArn: StrictStr | None = None
    Description: StrictStr | None = None
    DocumentMetadataConfigurationUpdates: list[KendraDocumentMetadataConfiguration] | None = None
    CapacityUnits: KendraCapacityUnitsConfiguration | None = None
    UserTokenConfigurations: list[KendraUserTokenConfiguration] | None = None
    UserContextPolicy: Literal['ATTRIBUTE_FILTER', 'USER_TOKEN'] | None = None
    UserGroupResolutionConfiguration: KendraUserGroupResolutionConfiguration | None = None
