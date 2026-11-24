from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .open_search_app_config import OpenSearchAppConfig
from .open_search_data_source import OpenSearchDataSource
from .open_search_iam_identity_center_options import OpenSearchIamIdentityCenterOptions


class OpenSearchUpdateApplicationResponse(BaseModel):
    id: StrictStr | None = None
    name: StrictStr | None = None
    arn: StrictStr | None = None
    dataSources: list[OpenSearchDataSource] | None = None
    iamIdentityCenterOptions: OpenSearchIamIdentityCenterOptions | None = None
    appConfigs: list[OpenSearchAppConfig] | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    lastUpdatedAt: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
