from werkflow_aws.models.codeguru import (
    CodeGuruAssociateRepositoryRequest,
    CodeGuruAssociateRepositoryResponse,
    CodeGuruCreateCodeReviewRequest,
    CodeGuruCreateCodeReviewResponse,
    CodeGuruDescribeCodeReviewRequest,
    CodeGuruDescribeCodeReviewResponse,
    CodeGuruDescribeRecommendationFeedbackRequest,
    CodeGuruDescribeRecommendationFeedbackResponse,
    CodeGuruDescribeRepositoryAssociationRequest,
    CodeGuruDescribeRepositoryAssociationResponse,
    CodeGuruDisassociateRepositoryRequest,
    CodeGuruDisassociateRepositoryResponse,
    CodeGuruListCodeReviewsRequest,
    CodeGuruListCodeReviewsResponse,
    CodeGuruListRecommendationFeedbackRequest,
    CodeGuruListRecommendationFeedbackResponse,
    CodeGuruListRecommendationsRequest,
    CodeGuruListRecommendationsResponse,
    CodeGuruListRepositoryAssociationsRequest,
    CodeGuruListRepositoryAssociationsResponse,
    CodeGuruListTagsForResourceRequest,
    CodeGuruListTagsForResourceResponse,
    CodeGuruPutRecommendationFeedbackRequest,
    CodeGuruPutRecommendationFeedbackResponse,
    CodeGuruTagResourceRequest,
    CodeGuruTagResourceResponse,
    CodeGuruUntagResourceRequest,
    CodeGuruUntagResourceResponse,
)
from werkflow_aws.types.codeguru_client import CodeGuruClient
from .base import AWSBaseService


class AWSCodeGuru(AWSBaseService[CodeGuruClient]):
    service_name = 'codeguru'
    boto3_service_name = 'codeguru-reviewer'

    def __init__(self) -> None:
        super().__init__(service_name='codeguru', boto3_service_name='codeguru-reviewer')

    async def associate_repository(
        self,
        request: CodeGuruAssociateRepositoryRequest,
    ) -> CodeGuruAssociateRepositoryResponse:
        client = self._require_client()
        return await self._execute(client.associate_repository, request, CodeGuruAssociateRepositoryResponse)

    async def create_code_review(
        self,
        request: CodeGuruCreateCodeReviewRequest,
    ) -> CodeGuruCreateCodeReviewResponse:
        client = self._require_client()
        return await self._execute(client.create_code_review, request, CodeGuruCreateCodeReviewResponse)

    async def describe_code_review(
        self,
        request: CodeGuruDescribeCodeReviewRequest,
    ) -> CodeGuruDescribeCodeReviewResponse:
        client = self._require_client()
        return await self._execute(client.describe_code_review, request, CodeGuruDescribeCodeReviewResponse)

    async def describe_recommendation_feedback(
        self,
        request: CodeGuruDescribeRecommendationFeedbackRequest,
    ) -> CodeGuruDescribeRecommendationFeedbackResponse:
        client = self._require_client()
        return await self._execute(client.describe_recommendation_feedback, request, CodeGuruDescribeRecommendationFeedbackResponse)

    async def describe_repository_association(
        self,
        request: CodeGuruDescribeRepositoryAssociationRequest,
    ) -> CodeGuruDescribeRepositoryAssociationResponse:
        client = self._require_client()
        return await self._execute(client.describe_repository_association, request, CodeGuruDescribeRepositoryAssociationResponse)

    async def disassociate_repository(
        self,
        request: CodeGuruDisassociateRepositoryRequest,
    ) -> CodeGuruDisassociateRepositoryResponse:
        client = self._require_client()
        return await self._execute(client.disassociate_repository, request, CodeGuruDisassociateRepositoryResponse)

    async def list_code_reviews(
        self,
        request: CodeGuruListCodeReviewsRequest,
    ) -> CodeGuruListCodeReviewsResponse:
        client = self._require_client()
        return await self._execute(client.list_code_reviews, request, CodeGuruListCodeReviewsResponse)

    async def list_recommendation_feedback(
        self,
        request: CodeGuruListRecommendationFeedbackRequest,
    ) -> CodeGuruListRecommendationFeedbackResponse:
        client = self._require_client()
        return await self._execute(client.list_recommendation_feedback, request, CodeGuruListRecommendationFeedbackResponse)

    async def list_recommendations(
        self,
        request: CodeGuruListRecommendationsRequest,
    ) -> CodeGuruListRecommendationsResponse:
        client = self._require_client()
        return await self._execute(client.list_recommendations, request, CodeGuruListRecommendationsResponse)

    async def list_repository_associations(
        self,
        request: CodeGuruListRepositoryAssociationsRequest | None = None,
    ) -> CodeGuruListRepositoryAssociationsResponse:
        client = self._require_client()
        return await self._execute(client.list_repository_associations, request, CodeGuruListRepositoryAssociationsResponse)

    async def list_repository_associations_paginated(
        self,
        request: CodeGuruListRepositoryAssociationsRequest | None = None,
    ) -> list[CodeGuruListRepositoryAssociationsResponse]:
        return await self._paginate('list_repository_associations', request, CodeGuruListRepositoryAssociationsResponse)

    async def list_tags_for_resource(
        self,
        request: CodeGuruListTagsForResourceRequest,
    ) -> CodeGuruListTagsForResourceResponse:
        client = self._require_client()
        return await self._execute(client.list_tags_for_resource, request, CodeGuruListTagsForResourceResponse)

    async def put_recommendation_feedback(
        self,
        request: CodeGuruPutRecommendationFeedbackRequest,
    ) -> CodeGuruPutRecommendationFeedbackResponse:
        client = self._require_client()
        return await self._execute(client.put_recommendation_feedback, request, CodeGuruPutRecommendationFeedbackResponse)

    async def tag_resource(
        self,
        request: CodeGuruTagResourceRequest,
    ) -> CodeGuruTagResourceResponse:
        client = self._require_client()
        return await self._execute(client.tag_resource, request, CodeGuruTagResourceResponse)

    async def untag_resource(
        self,
        request: CodeGuruUntagResourceRequest,
    ) -> CodeGuruUntagResourceResponse:
        client = self._require_client()
        return await self._execute(client.untag_resource, request, CodeGuruUntagResourceResponse)
