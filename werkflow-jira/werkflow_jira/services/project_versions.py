from __future__ import annotations

from typing import Any
from ..models.api import (
    DeleteAndReplaceVersionBean,
    PageBeanVersion,
    Version,
    VersionIssueCounts,
    VersionMoveBean,
    VersionRelatedWork,
    VersionUnresolvedIssuesCount,
)
from .base import JiraBaseService


class ProjectVersionsService(JiraBaseService):
    """Jira Cloud REST API v3 — Project versions (15 operations)."""

    async def create_related_work(
        self,
        id: str,
        body: VersionRelatedWork | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> VersionRelatedWork:
        """POST /rest/api/3/version/{id}/relatedwork — Create related work"""
        response = await self._request(
            'POST',
            '/rest/api/3/version/{id}/relatedwork',
            path_params={'id': id},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, VersionRelatedWork)

    async def create_version(
        self,
        body: Version | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Version:
        """POST /rest/api/3/version — Create version"""
        response = await self._request(
            'POST',
            '/rest/api/3/version',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, Version)

    async def delete_and_replace_version(
        self,
        id: str,
        body: DeleteAndReplaceVersionBean | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """POST /rest/api/3/version/{id}/removeAndSwap — Delete and replace version"""
        response = await self._request(
            'POST',
            '/rest/api/3/version/{id}/removeAndSwap',
            path_params={'id': id},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)

    async def delete_related_work(
        self,
        version_id: str,
        related_work_id: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> None:
        """DELETE /rest/api/3/version/{versionId}/relatedwork/{relatedWorkId} — Delete related work"""
        response = await self._request(
            'DELETE',
            '/rest/api/3/version/{versionId}/relatedwork/{relatedWorkId}',
            path_params={'versionId': version_id, 'relatedWorkId': related_work_id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return None

    async def delete_version(
        self,
        id: str,
        *,
        move_fix_issues_to: str | None = None,
        move_affected_issues_to: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> None:
        """DELETE /rest/api/3/version/{id} — Delete version"""
        response = await self._request(
            'DELETE',
            '/rest/api/3/version/{id}',
            path_params={'id': id},
            query_params={'moveFixIssuesTo': move_fix_issues_to, 'moveAffectedIssuesTo': move_affected_issues_to},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return None

    async def get_project_versions(
        self,
        project_id_or_key: str,
        *,
        expand: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> list[Version]:
        """GET /rest/api/3/project/{projectIdOrKey}/versions — Get project versions"""
        response = await self._request(
            'GET',
            '/rest/api/3/project/{projectIdOrKey}/versions',
            path_params={'projectIdOrKey': project_id_or_key},
            query_params={'expand': expand},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model_list(response, Version)

    async def get_project_versions_paginated(
        self,
        project_id_or_key: str,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        order_by: str | None = None,
        query: str | None = None,
        status: str | None = None,
        expand: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> PageBeanVersion:
        """GET /rest/api/3/project/{projectIdOrKey}/version — Get project versions paginated"""
        response = await self._request(
            'GET',
            '/rest/api/3/project/{projectIdOrKey}/version',
            path_params={'projectIdOrKey': project_id_or_key},
            query_params={'startAt': start_at, 'maxResults': max_results, 'orderBy': order_by, 'query': query, 'status': status, 'expand': expand},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, PageBeanVersion)

    async def get_related_work(
        self,
        id: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> list[VersionRelatedWork]:
        """GET /rest/api/3/version/{id}/relatedwork — Get related work"""
        response = await self._request(
            'GET',
            '/rest/api/3/version/{id}/relatedwork',
            path_params={'id': id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model_list(response, VersionRelatedWork)

    async def get_version(
        self,
        id: str,
        *,
        expand: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Version:
        """GET /rest/api/3/version/{id} — Get version"""
        response = await self._request(
            'GET',
            '/rest/api/3/version/{id}',
            path_params={'id': id},
            query_params={'expand': expand},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, Version)

    async def get_version_related_issues(
        self,
        id: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> VersionIssueCounts:
        """GET /rest/api/3/version/{id}/relatedIssueCounts — Get version's related issues count"""
        response = await self._request(
            'GET',
            '/rest/api/3/version/{id}/relatedIssueCounts',
            path_params={'id': id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, VersionIssueCounts)

    async def get_version_unresolved_issues(
        self,
        id: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> VersionUnresolvedIssuesCount:
        """GET /rest/api/3/version/{id}/unresolvedIssueCount — Get version's unresolved issues count"""
        response = await self._request(
            'GET',
            '/rest/api/3/version/{id}/unresolvedIssueCount',
            path_params={'id': id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, VersionUnresolvedIssuesCount)

    async def merge_versions(
        self,
        id: str,
        move_issues_to: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """PUT /rest/api/3/version/{id}/mergeto/{moveIssuesTo} — Merge versions"""
        response = await self._request(
            'PUT',
            '/rest/api/3/version/{id}/mergeto/{moveIssuesTo}',
            path_params={'id': id, 'moveIssuesTo': move_issues_to},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)

    async def move_version(
        self,
        id: str,
        body: VersionMoveBean | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Version:
        """POST /rest/api/3/version/{id}/move — Move version"""
        response = await self._request(
            'POST',
            '/rest/api/3/version/{id}/move',
            path_params={'id': id},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, Version)

    async def update_related_work(
        self,
        id: str,
        body: VersionRelatedWork | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> VersionRelatedWork:
        """PUT /rest/api/3/version/{id}/relatedwork — Update related work"""
        response = await self._request(
            'PUT',
            '/rest/api/3/version/{id}/relatedwork',
            path_params={'id': id},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, VersionRelatedWork)

    async def update_version(
        self,
        id: str,
        body: Version | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Version:
        """PUT /rest/api/3/version/{id} — Update version"""
        response = await self._request(
            'PUT',
            '/rest/api/3/version/{id}',
            path_params={'id': id},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, Version)
