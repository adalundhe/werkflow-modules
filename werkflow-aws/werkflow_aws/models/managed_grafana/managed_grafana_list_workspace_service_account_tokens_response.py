from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .managed_grafana_service_account_token_summary import ManagedGrafanaServiceAccountTokenSummary


class ManagedGrafanaListWorkspaceServiceAccountTokensResponse(BaseModel):
    nextToken: StrictStr | None = None
    serviceAccountTokens: list[ManagedGrafanaServiceAccountTokenSummary] | None = None
    serviceAccountId: StrictStr | None = None
    workspaceId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
