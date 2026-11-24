from __future__ import annotations

from ..models.api import (
    FoundUsersAndGroups,
)
from .base import JiraBaseService


class GroupAndUserPickerService(JiraBaseService):
    """Jira Cloud REST API v3 — Group and user picker (1 operations)."""

    async def find_users_and_groups(
        self,
        query: str,
        *,
        max_results: int | None = None,
        show_avatar: bool | None = None,
        field_id: str | None = None,
        project_id: list[str] | None = None,
        issue_type_id: list[str] | None = None,
        avatar_size: str | None = None,
        case_insensitive: bool | None = None,
        exclude_connect_addons: bool | None = None,
        include_ai_agents: bool | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> FoundUsersAndGroups:
        """GET /rest/api/3/groupuserpicker — Find users and groups"""
        response = await self._request(
            'GET',
            '/rest/api/3/groupuserpicker',
            query_params={'query': query, 'maxResults': max_results, 'showAvatar': show_avatar, 'fieldId': field_id, 'projectId': project_id, 'issueTypeId': issue_type_id, 'avatarSize': avatar_size, 'caseInsensitive': case_insensitive, 'excludeConnectAddons': exclude_connect_addons, 'includeAiAgents': include_ai_agents},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, FoundUsersAndGroups)
