from __future__ import annotations

from typing import Any
from ..models.api import (
    Comment,
    IssueCommentListRequestBean,
    PageBeanComment,
    PageOfComments,
)
from .base import JiraBaseService


class IssueCommentsService(JiraBaseService):
    """Jira Cloud REST API v3 — Issue comments (6 operations)."""

    async def add_comment(
        self,
        issue_id_or_key: str,
        body: Comment | dict[str, Any],
        *,
        expand: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Comment:
        """POST /rest/api/3/issue/{issueIdOrKey}/comment — Add comment"""
        response = await self._request(
            'POST',
            '/rest/api/3/issue/{issueIdOrKey}/comment',
            path_params={'issueIdOrKey': issue_id_or_key},
            query_params={'expand': expand},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, Comment)

    async def delete_comment(
        self,
        issue_id_or_key: str,
        id: str,
        *,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> None:
        """DELETE /rest/api/3/issue/{issueIdOrKey}/comment/{id} — Delete comment"""
        response = await self._request(
            'DELETE',
            '/rest/api/3/issue/{issueIdOrKey}/comment/{id}',
            path_params={'issueIdOrKey': issue_id_or_key, 'id': id},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return None

    async def get_comment(
        self,
        issue_id_or_key: str,
        id: str,
        *,
        expand: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Comment:
        """GET /rest/api/3/issue/{issueIdOrKey}/comment/{id} — Get comment"""
        response = await self._request(
            'GET',
            '/rest/api/3/issue/{issueIdOrKey}/comment/{id}',
            path_params={'issueIdOrKey': issue_id_or_key, 'id': id},
            query_params={'expand': expand},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, Comment)

    async def get_comments(
        self,
        issue_id_or_key: str,
        *,
        start_at: int | None = None,
        max_results: int | None = None,
        order_by: str | None = None,
        expand: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> PageOfComments:
        """GET /rest/api/3/issue/{issueIdOrKey}/comment — Get comments"""
        response = await self._request(
            'GET',
            '/rest/api/3/issue/{issueIdOrKey}/comment',
            path_params={'issueIdOrKey': issue_id_or_key},
            query_params={'startAt': start_at, 'maxResults': max_results, 'orderBy': order_by, 'expand': expand},
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, PageOfComments)

    async def get_comments_by_ids(
        self,
        body: IssueCommentListRequestBean | dict[str, Any],
        *,
        expand: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> PageBeanComment:
        """POST /rest/api/3/comment/list — Get comments by IDs"""
        response = await self._request(
            'POST',
            '/rest/api/3/comment/list',
            query_params={'expand': expand},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, PageBeanComment)

    async def update_comment(
        self,
        issue_id_or_key: str,
        id: str,
        body: Comment | dict[str, Any],
        *,
        notify_users: bool | None = None,
        override_editable_flag: bool | None = None,
        expand: str | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> Comment:
        """PUT /rest/api/3/issue/{issueIdOrKey}/comment/{id} — Update comment"""
        response = await self._request(
            'PUT',
            '/rest/api/3/issue/{issueIdOrKey}/comment/{id}',
            path_params={'issueIdOrKey': issue_id_or_key, 'id': id},
            query_params={'notifyUsers': notify_users, 'overrideEditableFlag': override_editable_flag, 'expand': expand},
            body=body,
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )
        return self._parse_model(response, Comment)
