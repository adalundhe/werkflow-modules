from abc import ABC, abstractmethod
from typing import Any
from botocore.paginate import Paginator


class CodeGuruClient(ABC):

    @abstractmethod
    def associate_repository(
        self,
        *,
        Repository: dict[str, Any],
        ClientRequestToken: str | None = None,
        Tags: dict[str, str] | None = None,
        KMSKeyDetails: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_code_review(
        self,
        *,
        Name: str,
        RepositoryAssociationArn: str,
        Type: dict[str, Any],
        ClientRequestToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_code_review(
        self,
        *,
        CodeReviewArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_recommendation_feedback(
        self,
        *,
        CodeReviewArn: str,
        RecommendationId: str,
        UserId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_repository_association(
        self,
        *,
        AssociationArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_repository(
        self,
        *,
        AssociationArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_code_reviews(
        self,
        *,
        Type: str,
        ProviderTypes: list[str] | None = None,
        States: list[str] | None = None,
        RepositoryNames: list[str] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_recommendation_feedback(
        self,
        *,
        CodeReviewArn: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
        UserIds: list[str] | None = None,
        RecommendationIds: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_recommendations(
        self,
        *,
        CodeReviewArn: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_repository_associations(
        self,
        *,
        ProviderTypes: list[str] | None = None,
        States: list[str] | None = None,
        Names: list[str] | None = None,
        Owners: list[str] | None = None,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_tags_for_resource(
        self,
        *,
        resourceArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_recommendation_feedback(
        self,
        *,
        CodeReviewArn: str,
        RecommendationId: str,
        Reactions: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def tag_resource(
        self,
        *,
        resourceArn: str,
        Tags: dict[str, str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def untag_resource(
        self,
        *,
        resourceArn: str,
        TagKeys: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
