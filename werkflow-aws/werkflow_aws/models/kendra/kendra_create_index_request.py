from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .kendra_server_side_encryption_configuration import KendraServerSideEncryptionConfiguration
from .kendra_tag import KendraTag
from .kendra_user_group_resolution_configuration import KendraUserGroupResolutionConfiguration
from .kendra_user_token_configuration import KendraUserTokenConfiguration


class KendraCreateIndexRequest(BaseModel):
    Name: StrictStr
    RoleArn: StrictStr
    Edition: Literal['DEVELOPER_EDITION', 'ENTERPRISE_EDITION', 'GEN_AI_ENTERPRISE_EDITION'] | None = None
    ServerSideEncryptionConfiguration: KendraServerSideEncryptionConfiguration | None = None
    Description: StrictStr | None = None
    ClientToken: StrictStr | None = None
    Tags: list[KendraTag] | None = None
    UserTokenConfigurations: list[KendraUserTokenConfiguration] | None = None
    UserContextPolicy: Literal['ATTRIBUTE_FILTER', 'USER_TOKEN'] | None = None
    UserGroupResolutionConfiguration: KendraUserGroupResolutionConfiguration | None = None
