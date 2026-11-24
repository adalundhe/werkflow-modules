from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .open_search_app_config import OpenSearchAppConfig
from .open_search_data_source import OpenSearchDataSource
from .open_search_iam_identity_center_options_input import OpenSearchIamIdentityCenterOptionsInput
from .open_search_tag import OpenSearchTag


class OpenSearchCreateApplicationRequest(BaseModel):
    name: StrictStr
    clientToken: StrictStr | None = None
    dataSources: list[OpenSearchDataSource] | None = None
    iamIdentityCenterOptions: OpenSearchIamIdentityCenterOptionsInput | None = None
    appConfigs: list[OpenSearchAppConfig] | None = None
    tagList: list[OpenSearchTag] | None = None
    kmsKeyArn: StrictStr | None = None
