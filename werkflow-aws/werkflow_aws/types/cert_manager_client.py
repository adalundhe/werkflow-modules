from abc import ABC, abstractmethod
from typing import Any, BinaryIO
from botocore.paginate import Paginator


class ACMClient(ABC):

    @abstractmethod
    def add_tags_to_certificate(
        self,
        *,
        CertificateArn: str,
        Tags: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_acme_domain_validation(
        self,
        *,
        AcmeEndpointArn: str,
        DomainName: str,
        PrevalidationOptions: dict[str, Any],
        IdempotencyToken: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_acme_endpoint(
        self,
        *,
        AuthorizationBehavior: str,
        CertificateAuthority: dict[str, Any],
        IdempotencyToken: str | None = None,
        Contact: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
        CertificateTags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_acme_external_account_binding(
        self,
        *,
        AcmeEndpointArn: str,
        RoleArn: str,
        IdempotencyToken: str | None = None,
        Expiration: dict[str, Any] | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_acme_domain_validation(
        self,
        *,
        AcmeDomainValidationArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_acme_endpoint(
        self,
        *,
        AcmeEndpointArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_acme_external_account_binding(
        self,
        *,
        AcmeExternalAccountBindingArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_certificate(
        self,
        *,
        CertificateArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_acme_account(
        self,
        *,
        AcmeEndpointArn: str,
        AccountUrl: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_acme_domain_validation(
        self,
        *,
        AcmeDomainValidationArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_acme_endpoint(
        self,
        *,
        AcmeEndpointArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_acme_external_account_binding(
        self,
        *,
        AcmeExternalAccountBindingArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_certificate(
        self,
        *,
        CertificateArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def export_certificate(
        self,
        *,
        CertificateArn: str,
        Passphrase: bytes | BinaryIO | str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_account_configuration(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_acme_external_account_binding_credentials(
        self,
        *,
        AcmeExternalAccountBindingArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_certificate(
        self,
        *,
        CertificateArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def import_certificate(
        self,
        *,
        Certificate: bytes | BinaryIO | str,
        PrivateKey: bytes | BinaryIO | str,
        CertificateArn: str | None = None,
        CertificateChain: bytes | BinaryIO | str | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_acme_accounts(
        self,
        *,
        AcmeEndpointArn: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_acme_domain_validations(
        self,
        *,
        AcmeEndpointArn: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_acme_endpoints(
        self,
        *,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_acme_external_account_bindings(
        self,
        *,
        AcmeEndpointArn: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_certificate_domain_validations(
        self,
        *,
        CertificateArn: str,
        NextToken: str | None = None,
        MaxItems: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_certificates(
        self,
        *,
        CertificateStatuses: list[str] | None = None,
        CertificateKeyPairOrigins: list[str] | None = None,
        RootHierarchyTypes: list[str] | None = None,
        Includes: dict[str, Any] | None = None,
        NextToken: str | None = None,
        MaxItems: int | None = None,
        SortBy: str | None = None,
        SortOrder: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_tags_for_certificate(
        self,
        *,
        CertificateArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_tags_for_resource(
        self,
        *,
        ResourceArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_account_configuration(
        self,
        *,
        IdempotencyToken: str,
        ExpiryEvents: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def remove_tags_from_certificate(
        self,
        *,
        CertificateArn: str,
        Tags: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def renew_certificate(
        self,
        *,
        CertificateArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def request_certificate(
        self,
        *,
        DomainName: str,
        ValidationMethod: str | None = None,
        SubjectAlternativeNames: list[str] | None = None,
        IdempotencyToken: str | None = None,
        DomainValidationOptions: list[dict[str, Any]] | None = None,
        Options: dict[str, Any] | None = None,
        CertificateAuthorityArn: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
        KeyAlgorithm: str | None = None,
        ManagedBy: str | None = None,
        CertificateUsage: str | None = None,
        RootHierarchyType: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def resend_validation_email(
        self,
        *,
        CertificateArn: str,
        Domain: str,
        ValidationDomain: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def revoke_acme_account(
        self,
        *,
        AcmeEndpointArn: str,
        AccountUrl: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def revoke_acme_external_account_binding(
        self,
        *,
        AcmeExternalAccountBindingArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def revoke_certificate(
        self,
        *,
        CertificateArn: str,
        RevocationReason: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def search_certificates(
        self,
        *,
        FilterStatement: dict[str, Any] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        SortBy: str | None = None,
        SortOrder: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def tag_resource(
        self,
        *,
        ResourceArn: str,
        Tags: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def untag_resource(
        self,
        *,
        ResourceArn: str,
        TagKeys: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_acme_domain_validation(
        self,
        *,
        AcmeDomainValidationArn: str,
        PrevalidationOptions: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_acme_endpoint(
        self,
        *,
        AcmeEndpointArn: str,
        AuthorizationBehavior: str | None = None,
        Contact: str | None = None,
        CertificateAuthority: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_certificate_options(
        self,
        *,
        CertificateArn: str,
        Options: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
