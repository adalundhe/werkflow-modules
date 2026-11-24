from abc import ABC, abstractmethod
from typing import Any
from botocore.paginate import Paginator


class STSClient(ABC):

    @abstractmethod
    def assume_role(
        self,
        *,
        RoleArn: str,
        RoleSessionName: str,
        PolicyArns: list[dict[str, Any]] | None = None,
        Policy: str | None = None,
        DurationSeconds: int | None = None,
        Tags: list[dict[str, Any]] | None = None,
        TransitiveTagKeys: list[str] | None = None,
        ExternalId: str | None = None,
        SerialNumber: str | None = None,
        TokenCode: str | None = None,
        SourceIdentity: str | None = None,
        ProvidedContexts: list[dict[str, Any]] | None = None,
        MinimumSessionTokenSize: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def assume_role_with_web_identity(
        self,
        *,
        RoleArn: str,
        RoleSessionName: str,
        WebIdentityToken: str,
        ProviderId: str | None = None,
        PolicyArns: list[dict[str, Any]] | None = None,
        Policy: str | None = None,
        DurationSeconds: int | None = None,
        MinimumSessionTokenSize: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_caller_identity(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_session_token(
        self,
        *,
        DurationSeconds: int | None = None,
        SerialNumber: str | None = None,
        TokenCode: str | None = None,
        MinimumSessionTokenSize: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def decode_authorization_message(
        self,
        *,
        EncodedMessage: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_access_key_info(
        self,
        *,
        AccessKeyId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def assume_role_with_saml(
        self,
        *,
        RoleArn: str,
        PrincipalArn: str,
        SAMLAssertion: str,
        PolicyArns: list[dict[str, Any]] | None = None,
        Policy: str | None = None,
        DurationSeconds: int | None = None,
        MinimumSessionTokenSize: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def assume_root(
        self,
        *,
        TargetPrincipal: str,
        TaskPolicyArn: dict[str, Any],
        DurationSeconds: int | None = None,
        MinimumSessionTokenSize: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_delegated_access_token(
        self,
        *,
        TradeInToken: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_federation_token(
        self,
        *,
        Name: str,
        Policy: str | None = None,
        PolicyArns: list[dict[str, Any]] | None = None,
        DurationSeconds: int | None = None,
        Tags: list[dict[str, Any]] | None = None,
        MinimumSessionTokenSize: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_scoped_credentials(
        self,
        *,
        Policy: str | None = None,
        DurationSeconds: int | None = None,
        MinimumSessionTokenSize: int | None = None,
        ScopedSessionDescription: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_web_identity_token(
        self,
        *,
        Audience: list[str],
        SigningAlgorithm: str,
        DurationSeconds: int | None = None,
        Scope: str | None = None,
        SubjectMode: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
