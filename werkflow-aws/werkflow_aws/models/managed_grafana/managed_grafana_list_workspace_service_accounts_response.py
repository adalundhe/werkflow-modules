from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .managed_grafana_service_account_summary import ManagedGrafanaServiceAccountSummary


class ManagedGrafanaListWorkspaceServiceAccountsResponse(BaseModel):
    nextToken: StrictStr | None = None
    serviceAccounts: list[ManagedGrafanaServiceAccountSummary] | None = None
    workspaceId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
