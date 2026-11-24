from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .open_search_app_config import OpenSearchAppConfig
from .open_search_data_source import OpenSearchDataSource
from .open_search_iam_identity_center_options_input import OpenSearchIamIdentityCenterOptionsInput


class OpenSearchUpdateApplicationRequest(BaseModel):
    id: StrictStr
    dataSources: list[OpenSearchDataSource] | None = None
    appConfigs: list[OpenSearchAppConfig] | None = None
    iamIdentityCenterOptions: OpenSearchIamIdentityCenterOptionsInput | None = None
