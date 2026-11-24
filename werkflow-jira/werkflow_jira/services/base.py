from __future__ import annotations

from collections.abc import Callable, Mapping, Sequence
from typing import Any, TypeVar
from urllib.parse import quote, urlencode

from pydantic import BaseModel, TypeAdapter
from werkflow_http import HTTP
from werkflow_http.connections.http.models.http import HTTPResponse
from werkflow_http.request import Data, File

ModelT = TypeVar("ModelT", bound=BaseModel)
AnyT = TypeVar("AnyT")


class JiraBaseService:
    """Shared async HTTP dispatch and Pydantic v2 deserialization for Jira Cloud REST API v3 services."""

    def __init__(
        self,
        client: HTTP,
        check_response: Callable[[HTTPResponse], HTTPResponse],
        get_default_credentials: Callable[[], tuple[str | None, str | None, str | None]],
    ) -> None:
        self._client = client
        self._check_response = check_response
        self._get_default_credentials = get_default_credentials

    def _resolve_credentials(
        self,
        jira_organization: str | None,
        jira_email: str | None,
        jira_api_token: str | None,
    ) -> tuple[str, str, str]:
        default_org, default_email, default_token = self._get_default_credentials()
        organization = jira_organization if jira_organization is not None else default_org
        email = jira_email if jira_email is not None else default_email
        api_token = jira_api_token if jira_api_token is not None else default_token

        missing: list[str] = []
        if not organization:
            missing.append("jira_organization")
        if not email:
            missing.append("jira_email")
        if not api_token:
            missing.append("jira_api_token")

        if missing:
            missing_str = ", ".join(missing)
            raise ValueError(
                f"Missing Jira credentials ({missing_str}). "
                "Call jira.configure(organization=..., email=..., api_token=...) "
                "or pass them to the service method."
            )

        assert organization is not None
        assert email is not None
        assert api_token is not None
        return organization, email, api_token

    @staticmethod
    def _build_base_url(organization: str) -> str:
        org = organization.strip().rstrip("/")
        if org.startswith("https://") or org.startswith("http://"):
            return org
        if "." in org:
            return f"https://{org}"
        return f"https://{org}.atlassian.net"

    @staticmethod
    def _format_path(
        path_template: str,
        path_params: Mapping[str, Any] | None,
    ) -> str:
        if not path_params:
            return path_template
        path = path_template
        for key, value in path_params.items():
            encoded = quote(str(value), safe="")
            path = path.replace("{" + key + "}", encoded)
        return path

    @staticmethod
    def _encode_query(
        query_params: Mapping[str, Any] | None,
    ) -> str:
        if not query_params:
            return ""
        pairs: list[tuple[str, str]] = []
        for key, value in query_params.items():
            if value is None:
                continue
            if isinstance(value, bool):
                pairs.append((key, "true" if value else "false"))
            elif isinstance(value, (list, tuple, set)):
                for item in value:
                    if item is None:
                        continue
                    if isinstance(item, bool):
                        pairs.append((key, "true" if item else "false"))
                    else:
                        pairs.append((key, str(item)))
            else:
                pairs.append((key, str(value)))
        if not pairs:
            return ""
        return urlencode(pairs, doseq=True)

    @staticmethod
    def _serialize_body(body: Any) -> Data:
        if body is None:
            return None
        if isinstance(body, BaseModel):
            return body.model_dump(mode="json", by_alias=True, exclude_none=True)
        if isinstance(body, list):
            return [
                item.model_dump(mode="json", by_alias=True, exclude_none=True)
                if isinstance(item, BaseModel)
                else item
                for item in body
            ]
        return body

    async def _request(
        self,
        method: str,
        path_template: str,
        *,
        path_params: Mapping[str, Any] | None = None,
        query_params: Mapping[str, Any] | None = None,
        headers: Mapping[str, Any] | None = None,
        body: Any = None,
        content_type: str | None = "application/json",
        accept: str | None = "application/json",
        files: Sequence[File | str | dict[str, Any]] | None = None,
        jira_organization: str | None = None,
        jira_email: str | None = None,
        jira_api_token: str | None = None,
    ) -> HTTPResponse:
        organization, email, api_token = self._resolve_credentials(
            jira_organization=jira_organization,
            jira_email=jira_email,
            jira_api_token=jira_api_token,
        )

        base_url = self._build_base_url(organization)
        path = self._format_path(path_template, path_params)
        query_string = self._encode_query(query_params)
        url = f"{base_url}{path}"
        if query_string:
            separator = "&" if "?" in url else "?"
            url = f"{url}{separator}{query_string}"

        req_headers: dict[str, int | float | str | bytes | None] = {}
        if accept:
            req_headers["Accept"] = accept
        if headers:
            for key, value in headers.items():
                if value is not None:
                    req_headers[key] = value

        serialized_body = self._serialize_body(body)
        if (
            serialized_body is not None
            and content_type is not None
            and files is None
            and not any(k.lower() == "content-type" for k in req_headers)
        ):
            req_headers["Content-Type"] = content_type

        auth = (email, api_token)
        method_upper = method.upper()

        if method_upper == "GET":
            response = await self._client.get(
                url,
                auth=auth,
                headers=req_headers or None,
            )
        elif method_upper == "POST":
            response = await self._client.post(
                url,
                auth=auth,
                headers=req_headers or None,
                data=serialized_body,
                files=files,
            )
        elif method_upper == "PUT":
            response = await self._client.put(
                url,
                auth=auth,
                headers=req_headers or None,
                data=serialized_body,
                files=files,
            )
        elif method_upper == "PATCH":
            response = await self._client.patch(
                url,
                auth=auth,
                headers=req_headers or None,
                data=serialized_body,
                files=files,
            )
        elif method_upper == "DELETE":
            if serialized_body is not None:
                response = await self._client.delete(
                    url,
                    auth=auth,
                    headers=req_headers or None,
                    data=serialized_body,
                )
            else:
                response = await self._client.delete(
                    url,
                    auth=auth,
                    headers=req_headers or None,
                )
        else:
            raise ValueError(f"Unsupported HTTP method: {method}")

        return self._check_response(response)

    @staticmethod
    def _parse_json(response: HTTPResponse) -> Any:
        if not response.content:
            return None
        payload = response.json()
        if isinstance(payload, Exception):
            raise payload
        return payload

    @classmethod
    def _parse_model(
        cls,
        response: HTTPResponse,
        model_cls: type[ModelT],
    ) -> ModelT:
        payload = cls._parse_json(response)
        if payload is None:
            payload = {}
        return model_cls.model_validate(payload)

    @classmethod
    def _parse_optional_model(
        cls,
        response: HTTPResponse,
        model_cls: type[ModelT],
    ) -> ModelT | None:
        payload = cls._parse_json(response)
        if payload is None:
            return None
        return model_cls.model_validate(payload)

    @classmethod
    def _parse_model_list(
        cls,
        response: HTTPResponse,
        model_cls: type[ModelT],
    ) -> list[ModelT]:
        payload = cls._parse_json(response)
        if payload is None:
            return []
        return [model_cls.model_validate(item) for item in payload]

    @classmethod
    def _parse_adapter(
        cls,
        response: HTTPResponse,
        adapter: TypeAdapter[AnyT],
    ) -> AnyT:
        payload = cls._parse_json(response)
        return adapter.validate_python(payload)

    @classmethod
    def _parse_optional_adapter(
        cls,
        response: HTTPResponse,
        adapter: TypeAdapter[AnyT],
    ) -> AnyT | None:
        payload = cls._parse_json(response)
        if payload is None:
            return None
        return adapter.validate_python(payload)

    @staticmethod
    def _parse_bytes(response: HTTPResponse) -> bytes:
        return bytes(response.content)

    @staticmethod
    def _parse_text(response: HTTPResponse) -> str:
        return bytes(response.content).decode("utf-8", errors="replace")
