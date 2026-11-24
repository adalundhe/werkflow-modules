from __future__ import annotations

from typing import Any
from ..models.api import (
    AddSecuritySchemeLevelsRequestBean,
    AssociateSecuritySchemeWithProjectDetails,
    CreateIssueSecuritySchemeDetails,
    PageBeanIssueSecuritySchemeToProjectMapping,
    PageBeanSecurityLevel,
    PageBeanSecurityLevelMember,
    PageBeanSecuritySchemeWithProjects,
    SecurityScheme,
    SecuritySchemeId,
    SecuritySchemeMembersRequest,
    SecuritySchemes,
    SetDefaultLevelsRequest,
    UpdateIssueSecurityLevelDetails,
    UpdateIssueSecuritySchemeRequestBean,
)
from .base import JiraBaseService


class IssueSecuritySchemesService(JiraBaseService):
    """Jira Cloud REST API v3 — Issue security schemes (16 operations)."""

    async def add_security_level(
        self,
        scheme_id: str,
        body: AddSecuritySchemeLevelsRequestBean | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """PUT /rest/api/3/issuesecurityschemes/{schemeId}/level — Add issue security levels"""
        response = await self._request(
            'PUT',
            '/rest/api/3/issuesecurityschemes/{schemeId}/level',
            path_params={'schemeId': scheme_id},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)

    async def add_security_level_members(
        self,
        scheme_id: str,
        level_id: str,
        body: SecuritySchemeMembersRequest | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """PUT /rest/api/3/issuesecurityschemes/{schemeId}/level/{levelId}/member — Add issue security level members"""
        response = await self._request(
            'PUT',
            '/rest/api/3/issuesecurityschemes/{schemeId}/level/{levelId}/member',
            path_params={'schemeId': scheme_id, 'levelId': level_id},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)

    async def associate_schemes_to_projects(
        self,
        body: AssociateSecuritySchemeWithProjectDetails | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> None:
        """PUT /rest/api/3/issuesecurityschemes/project — Associate security scheme to project"""
        response = await self._request(
            'PUT',
            '/rest/api/3/issuesecurityschemes/project',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return None

    async def create_issue_security_scheme(
        self,
        body: CreateIssueSecuritySchemeDetails | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> SecuritySchemeId:
        """POST /rest/api/3/issuesecurityschemes — Create issue security scheme"""
        response = await self._request(
            'POST',
            '/rest/api/3/issuesecurityschemes',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, SecuritySchemeId)

    async def delete_security_scheme(
        self,
        scheme_id: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """DELETE /rest/api/3/issuesecurityschemes/{schemeId} — Delete issue security scheme"""
        response = await self._request(
            'DELETE',
            '/rest/api/3/issuesecurityschemes/{schemeId}',
            path_params={'schemeId': scheme_id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)

    async def get_issue_security_scheme(
        self,
        id: int,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> SecurityScheme:
        """GET /rest/api/3/issuesecurityschemes/{id} — Get issue security scheme"""
        response = await self._request(
            'GET',
            '/rest/api/3/issuesecurityschemes/{id}',
            path_params={'id': id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, SecurityScheme)

    async def get_issue_security_schemes(
        self,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> SecuritySchemes:
        """GET /rest/api/3/issuesecurityschemes — Get issue security schemes"""
        response = await self._request(
            'GET',
            '/rest/api/3/issuesecurityschemes',
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, SecuritySchemes)

    async def get_security_level_members(
        self,
        *,
        start_at: str | None = None,
        max_results: str | None = None,
        id: list[str] | None = None,
        scheme_id: list[str] | None = None,
        level_id: list[str] | None = None,
        expand: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> PageBeanSecurityLevelMember:
        """GET /rest/api/3/issuesecurityschemes/level/member — Get issue security level members"""
        response = await self._request(
            'GET',
            '/rest/api/3/issuesecurityschemes/level/member',
            query_params={'startAt': start_at, 'maxResults': max_results, 'id': id, 'schemeId': scheme_id, 'levelId': level_id, 'expand': expand},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, PageBeanSecurityLevelMember)

    async def get_security_levels(
        self,
        *,
        start_at: str | None = None,
        max_results: str | None = None,
        id: list[str] | None = None,
        scheme_id: list[str] | None = None,
        only_default: bool | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> PageBeanSecurityLevel:
        """GET /rest/api/3/issuesecurityschemes/level — Get issue security levels"""
        response = await self._request(
            'GET',
            '/rest/api/3/issuesecurityschemes/level',
            query_params={'startAt': start_at, 'maxResults': max_results, 'id': id, 'schemeId': scheme_id, 'onlyDefault': only_default},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, PageBeanSecurityLevel)

    async def remove_level(
        self,
        scheme_id: str,
        level_id: str,
        *,
        replace_with: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> None:
        """DELETE /rest/api/3/issuesecurityschemes/{schemeId}/level/{levelId} — Remove issue security level"""
        response = await self._request(
            'DELETE',
            '/rest/api/3/issuesecurityschemes/{schemeId}/level/{levelId}',
            path_params={'schemeId': scheme_id, 'levelId': level_id},
            query_params={'replaceWith': replace_with},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return None

    async def remove_member_from_security_level(
        self,
        scheme_id: str,
        level_id: str,
        member_id: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """DELETE /rest/api/3/issuesecurityschemes/{schemeId}/level/{levelId}/member/{memberId} — Remove member from issue security level"""
        response = await self._request(
            'DELETE',
            '/rest/api/3/issuesecurityschemes/{schemeId}/level/{levelId}/member/{memberId}',
            path_params={'schemeId': scheme_id, 'levelId': level_id, 'memberId': member_id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)

    async def search_projects_using_security_schemes(
        self,
        *,
        start_at: str | None = None,
        max_results: str | None = None,
        issue_security_scheme_id: list[str] | None = None,
        project_id: list[str] | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> PageBeanIssueSecuritySchemeToProjectMapping:
        """GET /rest/api/3/issuesecurityschemes/project — Get projects using issue security schemes"""
        response = await self._request(
            'GET',
            '/rest/api/3/issuesecurityschemes/project',
            query_params={'startAt': start_at, 'maxResults': max_results, 'issueSecuritySchemeId': issue_security_scheme_id, 'projectId': project_id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, PageBeanIssueSecuritySchemeToProjectMapping)

    async def search_security_schemes(
        self,
        *,
        start_at: str | None = None,
        max_results: str | None = None,
        id: list[str] | None = None,
        project_id: list[str] | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> PageBeanSecuritySchemeWithProjects:
        """GET /rest/api/3/issuesecurityschemes/search — Search issue security schemes"""
        response = await self._request(
            'GET',
            '/rest/api/3/issuesecurityschemes/search',
            query_params={'startAt': start_at, 'maxResults': max_results, 'id': id, 'projectId': project_id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, PageBeanSecuritySchemeWithProjects)

    async def set_default_levels(
        self,
        body: SetDefaultLevelsRequest | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """PUT /rest/api/3/issuesecurityschemes/level/default — Set default issue security levels"""
        response = await self._request(
            'PUT',
            '/rest/api/3/issuesecurityschemes/level/default',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)

    async def update_issue_security_scheme(
        self,
        id: str,
        body: UpdateIssueSecuritySchemeRequestBean | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """PUT /rest/api/3/issuesecurityschemes/{id} — Update issue security scheme"""
        response = await self._request(
            'PUT',
            '/rest/api/3/issuesecurityschemes/{id}',
            path_params={'id': id},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)

    async def update_security_level(
        self,
        scheme_id: str,
        level_id: str,
        body: UpdateIssueSecurityLevelDetails | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """PUT /rest/api/3/issuesecurityschemes/{schemeId}/level/{levelId} — Update issue security level"""
        response = await self._request(
            'PUT',
            '/rest/api/3/issuesecurityschemes/{schemeId}/level/{levelId}',
            path_params={'schemeId': scheme_id, 'levelId': level_id},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)
