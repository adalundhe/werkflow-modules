from werkflow_aws.models.compute_optimizer import (
    ComputeOptimizerDeleteRecommendationPreferencesRequest,
    ComputeOptimizerDeleteRecommendationPreferencesResponse,
    ComputeOptimizerDescribeRecommendationExportJobsRequest,
    ComputeOptimizerDescribeRecommendationExportJobsResponse,
    ComputeOptimizerExportAutoScalingGroupRecommendationsRequest,
    ComputeOptimizerExportAutoScalingGroupRecommendationsResponse,
    ComputeOptimizerExportEBSVolumeRecommendationsRequest,
    ComputeOptimizerExportEBSVolumeRecommendationsResponse,
    ComputeOptimizerExportEC2InstanceRecommendationsRequest,
    ComputeOptimizerExportEC2InstanceRecommendationsResponse,
    ComputeOptimizerExportECSServiceRecommendationsRequest,
    ComputeOptimizerExportECSServiceRecommendationsResponse,
    ComputeOptimizerExportIdleRecommendationsRequest,
    ComputeOptimizerExportIdleRecommendationsResponse,
    ComputeOptimizerExportLambdaFunctionRecommendationsRequest,
    ComputeOptimizerExportLambdaFunctionRecommendationsResponse,
    ComputeOptimizerExportLicenseRecommendationsRequest,
    ComputeOptimizerExportLicenseRecommendationsResponse,
    ComputeOptimizerExportRDSDatabaseRecommendationsRequest,
    ComputeOptimizerExportRDSDatabaseRecommendationsResponse,
    ComputeOptimizerGetAutoScalingGroupRecommendationsRequest,
    ComputeOptimizerGetAutoScalingGroupRecommendationsResponse,
    ComputeOptimizerGetEBSVolumeRecommendationsRequest,
    ComputeOptimizerGetEBSVolumeRecommendationsResponse,
    ComputeOptimizerGetEC2InstanceRecommendationsRequest,
    ComputeOptimizerGetEC2InstanceRecommendationsResponse,
    ComputeOptimizerGetEC2RecommendationProjectedMetricsRequest,
    ComputeOptimizerGetEC2RecommendationProjectedMetricsResponse,
    ComputeOptimizerGetECSServiceRecommendationProjectedMetricsRequest,
    ComputeOptimizerGetECSServiceRecommendationProjectedMetricsResponse,
    ComputeOptimizerGetECSServiceRecommendationsRequest,
    ComputeOptimizerGetECSServiceRecommendationsResponse,
    ComputeOptimizerGetEffectiveRecommendationPreferencesRequest,
    ComputeOptimizerGetEffectiveRecommendationPreferencesResponse,
    ComputeOptimizerGetEnrollmentStatusRequest,
    ComputeOptimizerGetEnrollmentStatusResponse,
    ComputeOptimizerGetEnrollmentStatusesForOrganizationRequest,
    ComputeOptimizerGetEnrollmentStatusesForOrganizationResponse,
    ComputeOptimizerGetIdleRecommendationsRequest,
    ComputeOptimizerGetIdleRecommendationsResponse,
    ComputeOptimizerGetLambdaFunctionRecommendationsRequest,
    ComputeOptimizerGetLambdaFunctionRecommendationsResponse,
    ComputeOptimizerGetLicenseRecommendationsRequest,
    ComputeOptimizerGetLicenseRecommendationsResponse,
    ComputeOptimizerGetRDSDatabaseRecommendationProjectedMetricsRequest,
    ComputeOptimizerGetRDSDatabaseRecommendationProjectedMetricsResponse,
    ComputeOptimizerGetRDSDatabaseRecommendationsRequest,
    ComputeOptimizerGetRDSDatabaseRecommendationsResponse,
    ComputeOptimizerGetRecommendationPreferencesRequest,
    ComputeOptimizerGetRecommendationPreferencesResponse,
    ComputeOptimizerGetRecommendationSummariesRequest,
    ComputeOptimizerGetRecommendationSummariesResponse,
    ComputeOptimizerPutRecommendationPreferencesRequest,
    ComputeOptimizerPutRecommendationPreferencesResponse,
    ComputeOptimizerUpdateEnrollmentStatusRequest,
    ComputeOptimizerUpdateEnrollmentStatusResponse,
)
from werkflow_aws.types.compute_optimizer_client import ComputeOptimizerClient
from .base import AWSBaseService


class AWSComputeOptimizer(AWSBaseService[ComputeOptimizerClient]):
    service_name = 'compute-optimizer'
    boto3_service_name = 'compute-optimizer'

    def __init__(self) -> None:
        super().__init__(service_name='compute-optimizer', boto3_service_name='compute-optimizer')

    async def delete_recommendation_preferences(
        self,
        request: ComputeOptimizerDeleteRecommendationPreferencesRequest,
    ) -> ComputeOptimizerDeleteRecommendationPreferencesResponse:
        client = self._require_client()
        return await self._execute(client.delete_recommendation_preferences, request, ComputeOptimizerDeleteRecommendationPreferencesResponse)

    async def describe_recommendation_export_jobs(
        self,
        request: ComputeOptimizerDescribeRecommendationExportJobsRequest | None = None,
    ) -> ComputeOptimizerDescribeRecommendationExportJobsResponse:
        client = self._require_client()
        return await self._execute(client.describe_recommendation_export_jobs, request, ComputeOptimizerDescribeRecommendationExportJobsResponse)

    async def describe_recommendation_export_jobs_paginated(
        self,
        request: ComputeOptimizerDescribeRecommendationExportJobsRequest | None = None,
    ) -> list[ComputeOptimizerDescribeRecommendationExportJobsResponse]:
        return await self._paginate('describe_recommendation_export_jobs', request, ComputeOptimizerDescribeRecommendationExportJobsResponse)

    async def export_auto_scaling_group_recommendations(
        self,
        request: ComputeOptimizerExportAutoScalingGroupRecommendationsRequest,
    ) -> ComputeOptimizerExportAutoScalingGroupRecommendationsResponse:
        client = self._require_client()
        return await self._execute(client.export_auto_scaling_group_recommendations, request, ComputeOptimizerExportAutoScalingGroupRecommendationsResponse)

    async def export_ebs_volume_recommendations(
        self,
        request: ComputeOptimizerExportEBSVolumeRecommendationsRequest,
    ) -> ComputeOptimizerExportEBSVolumeRecommendationsResponse:
        client = self._require_client()
        return await self._execute(client.export_ebs_volume_recommendations, request, ComputeOptimizerExportEBSVolumeRecommendationsResponse)

    async def export_ec2_instance_recommendations(
        self,
        request: ComputeOptimizerExportEC2InstanceRecommendationsRequest,
    ) -> ComputeOptimizerExportEC2InstanceRecommendationsResponse:
        client = self._require_client()
        return await self._execute(client.export_ec2_instance_recommendations, request, ComputeOptimizerExportEC2InstanceRecommendationsResponse)

    async def export_ecs_service_recommendations(
        self,
        request: ComputeOptimizerExportECSServiceRecommendationsRequest,
    ) -> ComputeOptimizerExportECSServiceRecommendationsResponse:
        client = self._require_client()
        return await self._execute(client.export_ecs_service_recommendations, request, ComputeOptimizerExportECSServiceRecommendationsResponse)

    async def export_idle_recommendations(
        self,
        request: ComputeOptimizerExportIdleRecommendationsRequest,
    ) -> ComputeOptimizerExportIdleRecommendationsResponse:
        client = self._require_client()
        return await self._execute(client.export_idle_recommendations, request, ComputeOptimizerExportIdleRecommendationsResponse)

    async def export_lambda_function_recommendations(
        self,
        request: ComputeOptimizerExportLambdaFunctionRecommendationsRequest,
    ) -> ComputeOptimizerExportLambdaFunctionRecommendationsResponse:
        client = self._require_client()
        return await self._execute(client.export_lambda_function_recommendations, request, ComputeOptimizerExportLambdaFunctionRecommendationsResponse)

    async def export_license_recommendations(
        self,
        request: ComputeOptimizerExportLicenseRecommendationsRequest,
    ) -> ComputeOptimizerExportLicenseRecommendationsResponse:
        client = self._require_client()
        return await self._execute(client.export_license_recommendations, request, ComputeOptimizerExportLicenseRecommendationsResponse)

    async def export_rds_database_recommendations(
        self,
        request: ComputeOptimizerExportRDSDatabaseRecommendationsRequest,
    ) -> ComputeOptimizerExportRDSDatabaseRecommendationsResponse:
        client = self._require_client()
        return await self._execute(client.export_rds_database_recommendations, request, ComputeOptimizerExportRDSDatabaseRecommendationsResponse)

    async def get_auto_scaling_group_recommendations(
        self,
        request: ComputeOptimizerGetAutoScalingGroupRecommendationsRequest | None = None,
    ) -> ComputeOptimizerGetAutoScalingGroupRecommendationsResponse:
        client = self._require_client()
        return await self._execute(client.get_auto_scaling_group_recommendations, request, ComputeOptimizerGetAutoScalingGroupRecommendationsResponse)

    async def get_ebs_volume_recommendations(
        self,
        request: ComputeOptimizerGetEBSVolumeRecommendationsRequest | None = None,
    ) -> ComputeOptimizerGetEBSVolumeRecommendationsResponse:
        client = self._require_client()
        return await self._execute(client.get_ebs_volume_recommendations, request, ComputeOptimizerGetEBSVolumeRecommendationsResponse)

    async def get_ec2_instance_recommendations(
        self,
        request: ComputeOptimizerGetEC2InstanceRecommendationsRequest | None = None,
    ) -> ComputeOptimizerGetEC2InstanceRecommendationsResponse:
        client = self._require_client()
        return await self._execute(client.get_ec2_instance_recommendations, request, ComputeOptimizerGetEC2InstanceRecommendationsResponse)

    async def get_ec2_recommendation_projected_metrics(
        self,
        request: ComputeOptimizerGetEC2RecommendationProjectedMetricsRequest,
    ) -> ComputeOptimizerGetEC2RecommendationProjectedMetricsResponse:
        client = self._require_client()
        return await self._execute(client.get_ec2_recommendation_projected_metrics, request, ComputeOptimizerGetEC2RecommendationProjectedMetricsResponse)

    async def get_ecs_service_recommendation_projected_metrics(
        self,
        request: ComputeOptimizerGetECSServiceRecommendationProjectedMetricsRequest,
    ) -> ComputeOptimizerGetECSServiceRecommendationProjectedMetricsResponse:
        client = self._require_client()
        return await self._execute(client.get_ecs_service_recommendation_projected_metrics, request, ComputeOptimizerGetECSServiceRecommendationProjectedMetricsResponse)

    async def get_ecs_service_recommendations(
        self,
        request: ComputeOptimizerGetECSServiceRecommendationsRequest | None = None,
    ) -> ComputeOptimizerGetECSServiceRecommendationsResponse:
        client = self._require_client()
        return await self._execute(client.get_ecs_service_recommendations, request, ComputeOptimizerGetECSServiceRecommendationsResponse)

    async def get_effective_recommendation_preferences(
        self,
        request: ComputeOptimizerGetEffectiveRecommendationPreferencesRequest,
    ) -> ComputeOptimizerGetEffectiveRecommendationPreferencesResponse:
        client = self._require_client()
        return await self._execute(client.get_effective_recommendation_preferences, request, ComputeOptimizerGetEffectiveRecommendationPreferencesResponse)

    async def get_enrollment_status(
        self,
        request: ComputeOptimizerGetEnrollmentStatusRequest | None = None,
    ) -> ComputeOptimizerGetEnrollmentStatusResponse:
        client = self._require_client()
        return await self._execute(client.get_enrollment_status, request, ComputeOptimizerGetEnrollmentStatusResponse)

    async def get_enrollment_statuses_for_organization(
        self,
        request: ComputeOptimizerGetEnrollmentStatusesForOrganizationRequest | None = None,
    ) -> ComputeOptimizerGetEnrollmentStatusesForOrganizationResponse:
        client = self._require_client()
        return await self._execute(client.get_enrollment_statuses_for_organization, request, ComputeOptimizerGetEnrollmentStatusesForOrganizationResponse)

    async def get_enrollment_statuses_for_organization_paginated(
        self,
        request: ComputeOptimizerGetEnrollmentStatusesForOrganizationRequest | None = None,
    ) -> list[ComputeOptimizerGetEnrollmentStatusesForOrganizationResponse]:
        return await self._paginate('get_enrollment_statuses_for_organization', request, ComputeOptimizerGetEnrollmentStatusesForOrganizationResponse)

    async def get_idle_recommendations(
        self,
        request: ComputeOptimizerGetIdleRecommendationsRequest | None = None,
    ) -> ComputeOptimizerGetIdleRecommendationsResponse:
        client = self._require_client()
        return await self._execute(client.get_idle_recommendations, request, ComputeOptimizerGetIdleRecommendationsResponse)

    async def get_lambda_function_recommendations(
        self,
        request: ComputeOptimizerGetLambdaFunctionRecommendationsRequest | None = None,
    ) -> ComputeOptimizerGetLambdaFunctionRecommendationsResponse:
        client = self._require_client()
        return await self._execute(client.get_lambda_function_recommendations, request, ComputeOptimizerGetLambdaFunctionRecommendationsResponse)

    async def get_lambda_function_recommendations_paginated(
        self,
        request: ComputeOptimizerGetLambdaFunctionRecommendationsRequest | None = None,
    ) -> list[ComputeOptimizerGetLambdaFunctionRecommendationsResponse]:
        return await self._paginate('get_lambda_function_recommendations', request, ComputeOptimizerGetLambdaFunctionRecommendationsResponse)

    async def get_license_recommendations(
        self,
        request: ComputeOptimizerGetLicenseRecommendationsRequest | None = None,
    ) -> ComputeOptimizerGetLicenseRecommendationsResponse:
        client = self._require_client()
        return await self._execute(client.get_license_recommendations, request, ComputeOptimizerGetLicenseRecommendationsResponse)

    async def get_rds_database_recommendation_projected_metrics(
        self,
        request: ComputeOptimizerGetRDSDatabaseRecommendationProjectedMetricsRequest,
    ) -> ComputeOptimizerGetRDSDatabaseRecommendationProjectedMetricsResponse:
        client = self._require_client()
        return await self._execute(client.get_rds_database_recommendation_projected_metrics, request, ComputeOptimizerGetRDSDatabaseRecommendationProjectedMetricsResponse)

    async def get_rds_database_recommendations(
        self,
        request: ComputeOptimizerGetRDSDatabaseRecommendationsRequest | None = None,
    ) -> ComputeOptimizerGetRDSDatabaseRecommendationsResponse:
        client = self._require_client()
        return await self._execute(client.get_rds_database_recommendations, request, ComputeOptimizerGetRDSDatabaseRecommendationsResponse)

    async def get_recommendation_preferences(
        self,
        request: ComputeOptimizerGetRecommendationPreferencesRequest,
    ) -> ComputeOptimizerGetRecommendationPreferencesResponse:
        client = self._require_client()
        return await self._execute(client.get_recommendation_preferences, request, ComputeOptimizerGetRecommendationPreferencesResponse)

    async def get_recommendation_preferences_paginated(
        self,
        request: ComputeOptimizerGetRecommendationPreferencesRequest,
    ) -> list[ComputeOptimizerGetRecommendationPreferencesResponse]:
        return await self._paginate('get_recommendation_preferences', request, ComputeOptimizerGetRecommendationPreferencesResponse)

    async def get_recommendation_summaries(
        self,
        request: ComputeOptimizerGetRecommendationSummariesRequest | None = None,
    ) -> ComputeOptimizerGetRecommendationSummariesResponse:
        client = self._require_client()
        return await self._execute(client.get_recommendation_summaries, request, ComputeOptimizerGetRecommendationSummariesResponse)

    async def get_recommendation_summaries_paginated(
        self,
        request: ComputeOptimizerGetRecommendationSummariesRequest | None = None,
    ) -> list[ComputeOptimizerGetRecommendationSummariesResponse]:
        return await self._paginate('get_recommendation_summaries', request, ComputeOptimizerGetRecommendationSummariesResponse)

    async def put_recommendation_preferences(
        self,
        request: ComputeOptimizerPutRecommendationPreferencesRequest,
    ) -> ComputeOptimizerPutRecommendationPreferencesResponse:
        client = self._require_client()
        return await self._execute(client.put_recommendation_preferences, request, ComputeOptimizerPutRecommendationPreferencesResponse)

    async def update_enrollment_status(
        self,
        request: ComputeOptimizerUpdateEnrollmentStatusRequest,
    ) -> ComputeOptimizerUpdateEnrollmentStatusResponse:
        client = self._require_client()
        return await self._execute(client.update_enrollment_status, request, ComputeOptimizerUpdateEnrollmentStatusResponse)
