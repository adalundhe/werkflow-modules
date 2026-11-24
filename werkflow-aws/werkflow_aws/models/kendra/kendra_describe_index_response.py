from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .kendra_capacity_units_configuration import KendraCapacityUnitsConfiguration
from .kendra_document_metadata_configuration import KendraDocumentMetadataConfiguration
from .kendra_index_statistics import KendraIndexStatistics
from .kendra_server_side_encryption_configuration import KendraServerSideEncryptionConfiguration
from .kendra_user_group_resolution_configuration import KendraUserGroupResolutionConfiguration
from .kendra_user_token_configuration import KendraUserTokenConfiguration


class KendraDescribeIndexResponse(BaseModel):
    Name: StrictStr | None = None
    Id: StrictStr | None = None
    Edition: StrictStr | None = None
    RoleArn: StrictStr | None = None
    ServerSideEncryptionConfiguration: KendraServerSideEncryptionConfiguration | None = None
    Status: StrictStr | None = None
    Description: StrictStr | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
    UpdatedAt: datetime.datetime | StrictStr | None = None
    DocumentMetadataConfigurations: list[KendraDocumentMetadataConfiguration] | None = None
    IndexStatistics: KendraIndexStatistics | None = None
    ErrorMessage: StrictStr | None = None
    CapacityUnits: KendraCapacityUnitsConfiguration | None = None
    UserTokenConfigurations: list[KendraUserTokenConfiguration] | None = None
    UserContextPolicy: StrictStr | None = None
    UserGroupResolutionConfiguration: KendraUserGroupResolutionConfiguration | None = None
    ResponseMetadata: dict[str, Any] | None = None
