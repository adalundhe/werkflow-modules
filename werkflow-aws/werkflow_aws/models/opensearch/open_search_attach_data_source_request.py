from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .open_search_workspace_configuration_input import OpenSearchWorkspaceConfigurationInput


class OpenSearchAttachDataSourceRequest(BaseModel):
    id: StrictStr
    dataSourceArn: StrictStr
    workspaceId: StrictStr | None = None
    workspaceConfiguration: OpenSearchWorkspaceConfigurationInput | None = None
    clientToken: StrictStr | None = None
