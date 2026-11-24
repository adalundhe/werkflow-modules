from __future__ import annotations

from typing import Any
from ..models.api import (
    EditTemplateRequest,
    ProjectCustomTemplateCreateRequestDTO,
    ProjectTemplateModel,
    SaveTemplateRequest,
    SaveTemplateResponse,
)
from .base import JiraBaseService


class ProjectTemplatesService(JiraBaseService):
    """Jira Cloud REST API v3 — Project templates (5 operations)."""

    async def create_project_with_custom_template(
        self,
        body: ProjectCustomTemplateCreateRequestDTO | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> None:
        """POST /rest/api/3/project-template — Create custom project"""
        response = await self._request(
            'POST',
            '/rest/api/3/project-template',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return None

    async def edit_template(
        self,
        body: EditTemplateRequest | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """PUT /rest/api/3/project-template/edit-template — Edit a custom project template"""
        response = await self._request(
            'PUT',
            '/rest/api/3/project-template/edit-template',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)

    async def live_template(
        self,
        *,
        project_id: str | None = None,
        template_key: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> ProjectTemplateModel:
        """GET /rest/api/3/project-template/live-template — Gets a custom project template"""
        response = await self._request(
            'GET',
            '/rest/api/3/project-template/live-template',
            query_params={'projectId': project_id, 'templateKey': template_key},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, ProjectTemplateModel)

    async def remove_template(
        self,
        template_key: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Any:
        """DELETE /rest/api/3/project-template/remove-template — Deletes a custom project template"""
        response = await self._request(
            'DELETE',
            '/rest/api/3/project-template/remove-template',
            query_params={'templateKey': template_key},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_json(response)

    async def save_template(
        self,
        body: SaveTemplateRequest | dict[str, Any],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> SaveTemplateResponse:
        """POST /rest/api/3/project-template/save-template — Save a custom project template"""
        response = await self._request(
            'POST',
            '/rest/api/3/project-template/save-template',
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, SaveTemplateResponse)
