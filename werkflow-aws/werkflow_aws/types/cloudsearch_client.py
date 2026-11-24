from abc import ABC, abstractmethod
from typing import Any
from botocore.paginate import Paginator


class CloudSearchClient(ABC):

    @abstractmethod
    def build_suggesters(
        self,
        *,
        DomainName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_domain(
        self,
        *,
        DomainName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def define_analysis_scheme(
        self,
        *,
        DomainName: str,
        AnalysisScheme: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def define_expression(
        self,
        *,
        DomainName: str,
        Expression: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def define_index_field(
        self,
        *,
        DomainName: str,
        IndexField: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def define_suggester(
        self,
        *,
        DomainName: str,
        Suggester: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_analysis_scheme(
        self,
        *,
        DomainName: str,
        AnalysisSchemeName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_domain(
        self,
        *,
        DomainName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_expression(
        self,
        *,
        DomainName: str,
        ExpressionName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_index_field(
        self,
        *,
        DomainName: str,
        IndexFieldName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_suggester(
        self,
        *,
        DomainName: str,
        SuggesterName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_analysis_schemes(
        self,
        *,
        DomainName: str,
        AnalysisSchemeNames: list[str] | None = None,
        Deployed: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_availability_options(
        self,
        *,
        DomainName: str,
        Deployed: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_domain_endpoint_options(
        self,
        *,
        DomainName: str,
        Deployed: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_domains(
        self,
        *,
        DomainNames: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_expressions(
        self,
        *,
        DomainName: str,
        ExpressionNames: list[str] | None = None,
        Deployed: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_index_fields(
        self,
        *,
        DomainName: str,
        FieldNames: list[str] | None = None,
        Deployed: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_scaling_parameters(
        self,
        *,
        DomainName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_service_access_policies(
        self,
        *,
        DomainName: str,
        Deployed: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_suggesters(
        self,
        *,
        DomainName: str,
        SuggesterNames: list[str] | None = None,
        Deployed: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def index_documents(
        self,
        *,
        DomainName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_domain_names(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_availability_options(
        self,
        *,
        DomainName: str,
        MultiAZ: bool,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_domain_endpoint_options(
        self,
        *,
        DomainName: str,
        DomainEndpointOptions: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_scaling_parameters(
        self,
        *,
        DomainName: str,
        ScalingParameters: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_service_access_policies(
        self,
        *,
        DomainName: str,
        AccessPolicies: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
