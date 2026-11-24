from __future__ import annotations

from collections.abc import Sequence
from typing import Any
from werkflow_http.request import File
from ..models.api import (
    Attachment,
    AttachmentArchiveImpl,
    AttachmentArchiveMetadataReadable,
    AttachmentMetadata,
    AttachmentSettings,
)
from .base import JiraBaseService


class IssueAttachmentsService(JiraBaseService):
    """Jira Cloud REST API v3 — Issue attachments (8 operations)."""

    async def add_attachment(
        self,
        issue_id_or_key: str,
        files: Sequence[File | str | dict[str, Any]],
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> list[Attachment]:
        """POST /rest/api/3/issue/{issueIdOrKey}/attachments — Add attachment"""
        response = await self._request(
            'POST',
            '/rest/api/3/issue/{issueIdOrKey}/attachments',
            path_params={'issueIdOrKey': issue_id_or_key},
            headers={'X-Atlassian-Token': 'no-check'},
            files=files,
            content_type=None,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model_list(response, Attachment)

    async def expand_attachment_for_humans(
        self,
        id: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> AttachmentArchiveMetadataReadable:
        """GET /rest/api/3/attachment/{id}/expand/human — Get all metadata for an expanded attachment"""
        response = await self._request(
            'GET',
            '/rest/api/3/attachment/{id}/expand/human',
            path_params={'id': id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, AttachmentArchiveMetadataReadable)

    async def expand_attachment_for_machines(
        self,
        id: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> AttachmentArchiveImpl:
        """GET /rest/api/3/attachment/{id}/expand/raw — Get contents metadata for an expanded attachment"""
        response = await self._request(
            'GET',
            '/rest/api/3/attachment/{id}/expand/raw',
            path_params={'id': id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, AttachmentArchiveImpl)

    async def get_attachment(
        self,
        id: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> AttachmentMetadata:
        """GET /rest/api/3/attachment/{id} — Get attachment metadata"""
        response = await self._request(
            'GET',
            '/rest/api/3/attachment/{id}',
            path_params={'id': id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, AttachmentMetadata)

    async def get_attachment_content(
        self,
        id: str,
        *,
        redirect: bool | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> bytes:
        """GET /rest/api/3/attachment/content/{id} — Get attachment content"""
        response = await self._request(
            'GET',
            '/rest/api/3/attachment/content/{id}',
            path_params={'id': id},
            query_params={'redirect': redirect},
            accept="*/*",
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_bytes(response)

    async def get_attachment_meta(
        self,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> AttachmentSettings:
        """GET /rest/api/3/attachment/meta — Get Jira attachment settings"""
        response = await self._request(
            'GET',
            '/rest/api/3/attachment/meta',
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, AttachmentSettings)

    async def get_attachment_thumbnail(
        self,
        id: str,
        *,
        redirect: bool | None = None,
        fallback_to_default: bool | None = None,
        width: int | None = None,
        height: int | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> bytes:
        """GET /rest/api/3/attachment/thumbnail/{id} — Get attachment thumbnail"""
        response = await self._request(
            'GET',
            '/rest/api/3/attachment/thumbnail/{id}',
            path_params={'id': id},
            query_params={'redirect': redirect, 'fallbackToDefault': fallback_to_default, 'width': width, 'height': height},
            accept="*/*",
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_bytes(response)

    async def remove_attachment(
        self,
        id: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> None:
        """DELETE /rest/api/3/attachment/{id} — Delete attachment"""
        response = await self._request(
            'DELETE',
            '/rest/api/3/attachment/{id}',
            path_params={'id': id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return None
