from werkflow_aws.models.msk import (
    MSKCreateClusterRequest,
    MSKCreateClusterResponse,
    MSKDeleteClusterRequest,
    MSKDeleteClusterResponse,
    MSKDescribeClusterRequest,
    MSKDescribeClusterResponse,
    MSKDescribeClusterV2Request,
    MSKDescribeClusterV2Response,
    MSKDescribeConfigurationRequest,
    MSKDescribeConfigurationResponse,
    MSKEmptyResponse,
    MSKGetBootstrapBrokersRequest,
    MSKGetBootstrapBrokersResponse,
    MSKListClustersRequest,
    MSKListClustersResponse,
    MSKListClustersV2Request,
    MSKListClustersV2Response,
    MSKListConfigurationsRequest,
    MSKListConfigurationsResponse,
    MSKListNodesRequest,
    MSKListNodesResponse,
    MSKListTagsForResourceRequest,
    MSKListTagsForResourceResponse,
    MSKTagResourceRequest,
    MSKUntagResourceRequest,
)
from werkflow_aws.types import MSKClient
from .base import AWSBaseService
from werkflow_aws.models.msk import (
    MSKBatchAssociateScramSecretRequest,
    MSKBatchAssociateScramSecretResponse,
    MSKBatchDisassociateScramSecretRequest,
    MSKBatchDisassociateScramSecretResponse,
    MSKCreateAssessmentRequest,
    MSKCreateAssessmentResponse,
    MSKCreateChannelRequest,
    MSKCreateChannelResponse,
    MSKCreateClusterV2Request,
    MSKCreateClusterV2Response,
    MSKCreateConfigurationRequest,
    MSKCreateConfigurationResponse,
    MSKCreateReplicatorRequest,
    MSKCreateReplicatorResponse,
    MSKCreateTopicRequest,
    MSKCreateTopicResponse,
    MSKCreateVpcConnectionRequest,
    MSKCreateVpcConnectionResponse,
    MSKDeleteAssessmentRequest,
    MSKDeleteAssessmentResponse,
    MSKDeleteChannelRequest,
    MSKDeleteChannelResponse,
    MSKDeleteClusterPolicyRequest,
    MSKDeleteClusterPolicyResponse,
    MSKDeleteConfigurationRequest,
    MSKDeleteConfigurationResponse,
    MSKDeleteReplicatorRequest,
    MSKDeleteReplicatorResponse,
    MSKDeleteTopicRequest,
    MSKDeleteTopicResponse,
    MSKDeleteVpcConnectionRequest,
    MSKDeleteVpcConnectionResponse,
    MSKDescribeAssessmentRequest,
    MSKDescribeAssessmentResponse,
    MSKDescribeChannelRequest,
    MSKDescribeChannelResponse,
    MSKDescribeClusterOperationRequest,
    MSKDescribeClusterOperationResponse,
    MSKDescribeClusterOperationV2Request,
    MSKDescribeClusterOperationV2Response,
    MSKDescribeConfigurationRevisionRequest,
    MSKDescribeConfigurationRevisionResponse,
    MSKDescribeReplicatorRequest,
    MSKDescribeReplicatorResponse,
    MSKDescribeTopicPartitionsRequest,
    MSKDescribeTopicPartitionsResponse,
    MSKDescribeTopicReassignmentRequest,
    MSKDescribeTopicReassignmentResponse,
    MSKDescribeTopicRequest,
    MSKDescribeTopicResponse,
    MSKDescribeVpcConnectionRequest,
    MSKDescribeVpcConnectionResponse,
    MSKGetClusterPolicyRequest,
    MSKGetClusterPolicyResponse,
    MSKGetCompatibleKafkaVersionsRequest,
    MSKGetCompatibleKafkaVersionsResponse,
    MSKListAssessmentFindingsRequest,
    MSKListAssessmentFindingsResponse,
    MSKListAssessmentsRequest,
    MSKListAssessmentsResponse,
    MSKListChannelsRequest,
    MSKListChannelsResponse,
    MSKListClientVpcConnectionsRequest,
    MSKListClientVpcConnectionsResponse,
    MSKListClusterOperationsRequest,
    MSKListClusterOperationsResponse,
    MSKListClusterOperationsV2Request,
    MSKListClusterOperationsV2Response,
    MSKListConfigurationRevisionsRequest,
    MSKListConfigurationRevisionsResponse,
    MSKListKafkaVersionsRequest,
    MSKListKafkaVersionsResponse,
    MSKListReplicatorsRequest,
    MSKListReplicatorsResponse,
    MSKListScramSecretsRequest,
    MSKListScramSecretsResponse,
    MSKListTopicReassignmentsRequest,
    MSKListTopicReassignmentsResponse,
    MSKListTopicsRequest,
    MSKListTopicsResponse,
    MSKListVpcConnectionsRequest,
    MSKListVpcConnectionsResponse,
    MSKPutClusterPolicyRequest,
    MSKPutClusterPolicyResponse,
    MSKRebootBrokerRequest,
    MSKRebootBrokerResponse,
    MSKRejectClientVpcConnectionRequest,
    MSKRejectClientVpcConnectionResponse,
    MSKStartTopicReassignmentRequest,
    MSKStartTopicReassignmentResponse,
    MSKStopTopicReassignmentRequest,
    MSKStopTopicReassignmentResponse,
    MSKUpdateBrokerCountRequest,
    MSKUpdateBrokerCountResponse,
    MSKUpdateBrokerStorageRequest,
    MSKUpdateBrokerStorageResponse,
    MSKUpdateBrokerTypeRequest,
    MSKUpdateBrokerTypeResponse,
    MSKUpdateChannelRequest,
    MSKUpdateChannelResponse,
    MSKUpdateClusterConfigurationRequest,
    MSKUpdateClusterConfigurationResponse,
    MSKUpdateClusterKafkaVersionRequest,
    MSKUpdateClusterKafkaVersionResponse,
    MSKUpdateConfigurationRequest,
    MSKUpdateConfigurationResponse,
    MSKUpdateConnectivityRequest,
    MSKUpdateConnectivityResponse,
    MSKUpdateMonitoringRequest,
    MSKUpdateMonitoringResponse,
    MSKUpdateRebalancingRequest,
    MSKUpdateRebalancingResponse,
    MSKUpdateReplicationInfoRequest,
    MSKUpdateReplicationInfoResponse,
    MSKUpdateSecurityRequest,
    MSKUpdateSecurityResponse,
    MSKUpdateStorageRequest,
    MSKUpdateStorageResponse,
    MSKUpdateTopicRequest,
    MSKUpdateTopicResponse,
)


class AWSMSK(AWSBaseService[MSKClient]):
    service_name = 'MSK'
    boto3_service_name = 'kafka'

    def __init__(self) -> None:
        super().__init__(service_name='MSK', boto3_service_name='kafka')

    async def list_clusters(
        self,
        request: MSKListClustersRequest | None = None,
    ) -> MSKListClustersResponse:
        client = self._require_client()
        return await self._execute(
            client.list_clusters,
            request or MSKListClustersRequest(),
            MSKListClustersResponse,
        )

    async def list_clusters_paginated(
        self,
        request: MSKListClustersRequest | None = None,
    ) -> list[MSKListClustersResponse]:
        return await self._paginate(
            'list_clusters',
            request or MSKListClustersRequest(),
            MSKListClustersResponse,
        )

    async def list_clusters_v2(
        self,
        request: MSKListClustersV2Request | None = None,
    ) -> MSKListClustersV2Response:
        client = self._require_client()
        return await self._execute(
            client.list_clusters_v2,
            request or MSKListClustersV2Request(),
            MSKListClustersV2Response,
        )

    async def list_clusters_v2_paginated(
        self,
        request: MSKListClustersV2Request | None = None,
    ) -> list[MSKListClustersV2Response]:
        return await self._paginate(
            'list_clusters_v2',
            request or MSKListClustersV2Request(),
            MSKListClustersV2Response,
        )

    async def describe_cluster(
        self,
        request: MSKDescribeClusterRequest,
    ) -> MSKDescribeClusterResponse:
        client = self._require_client()
        return await self._execute(
            client.describe_cluster,
            request,
            MSKDescribeClusterResponse,
        )

    async def describe_cluster_v2(
        self,
        request: MSKDescribeClusterV2Request,
    ) -> MSKDescribeClusterV2Response:
        client = self._require_client()
        return await self._execute(
            client.describe_cluster_v2,
            request,
            MSKDescribeClusterV2Response,
        )

    async def get_bootstrap_brokers(
        self,
        request: MSKGetBootstrapBrokersRequest,
    ) -> MSKGetBootstrapBrokersResponse:
        client = self._require_client()
        return await self._execute(
            client.get_bootstrap_brokers,
            request,
            MSKGetBootstrapBrokersResponse,
        )

    async def list_nodes(
        self,
        request: MSKListNodesRequest,
    ) -> MSKListNodesResponse:
        client = self._require_client()
        return await self._execute(
            client.list_nodes,
            request,
            MSKListNodesResponse,
        )

    async def list_nodes_paginated(
        self,
        request: MSKListNodesRequest,
    ) -> list[MSKListNodesResponse]:
        return await self._paginate(
            'list_nodes',
            request,
            MSKListNodesResponse,
        )

    async def create_cluster(
        self,
        request: MSKCreateClusterRequest,
    ) -> MSKCreateClusterResponse:
        client = self._require_client()
        return await self._execute(
            client.create_cluster,
            request,
            MSKCreateClusterResponse,
        )

    async def delete_cluster(
        self,
        request: MSKDeleteClusterRequest,
    ) -> MSKDeleteClusterResponse:
        client = self._require_client()
        return await self._execute(
            client.delete_cluster,
            request,
            MSKDeleteClusterResponse,
        )

    async def list_configurations(
        self,
        request: MSKListConfigurationsRequest | None = None,
    ) -> MSKListConfigurationsResponse:
        client = self._require_client()
        return await self._execute(
            client.list_configurations,
            request or MSKListConfigurationsRequest(),
            MSKListConfigurationsResponse,
        )

    async def list_configurations_paginated(
        self,
        request: MSKListConfigurationsRequest | None = None,
    ) -> list[MSKListConfigurationsResponse]:
        return await self._paginate(
            'list_configurations',
            request or MSKListConfigurationsRequest(),
            MSKListConfigurationsResponse,
        )

    async def describe_configuration(
        self,
        request: MSKDescribeConfigurationRequest,
    ) -> MSKDescribeConfigurationResponse:
        client = self._require_client()
        return await self._execute(
            client.describe_configuration,
            request,
            MSKDescribeConfigurationResponse,
        )

    async def list_tags_for_resource(
        self,
        request: MSKListTagsForResourceRequest,
    ) -> MSKListTagsForResourceResponse:
        client = self._require_client()
        return await self._execute(
            client.list_tags_for_resource,
            request,
            MSKListTagsForResourceResponse,
        )

    async def tag_resource(
        self,
        request: MSKTagResourceRequest,
    ) -> MSKEmptyResponse:
        client = self._require_client()
        return await self._execute(
            client.tag_resource,
            request,
            MSKEmptyResponse,
        )

    async def untag_resource(
        self,
        request: MSKUntagResourceRequest,
    ) -> MSKEmptyResponse:
        client = self._require_client()
        return await self._execute(
            client.untag_resource,
            request,
            MSKEmptyResponse,
        )

    async def batch_associate_scram_secret(
        self,
        request: MSKBatchAssociateScramSecretRequest,
    ) -> MSKBatchAssociateScramSecretResponse:
        client = self._require_client()
        return await self._execute(client.batch_associate_scram_secret, request, MSKBatchAssociateScramSecretResponse)

    async def batch_disassociate_scram_secret(
        self,
        request: MSKBatchDisassociateScramSecretRequest,
    ) -> MSKBatchDisassociateScramSecretResponse:
        client = self._require_client()
        return await self._execute(client.batch_disassociate_scram_secret, request, MSKBatchDisassociateScramSecretResponse)

    async def create_assessment(
        self,
        request: MSKCreateAssessmentRequest,
    ) -> MSKCreateAssessmentResponse:
        client = self._require_client()
        return await self._execute(client.create_assessment, request, MSKCreateAssessmentResponse)

    async def create_channel(
        self,
        request: MSKCreateChannelRequest,
    ) -> MSKCreateChannelResponse:
        client = self._require_client()
        return await self._execute(client.create_channel, request, MSKCreateChannelResponse)

    async def create_cluster_v2(
        self,
        request: MSKCreateClusterV2Request,
    ) -> MSKCreateClusterV2Response:
        client = self._require_client()
        return await self._execute(client.create_cluster_v2, request, MSKCreateClusterV2Response)

    async def create_configuration(
        self,
        request: MSKCreateConfigurationRequest,
    ) -> MSKCreateConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.create_configuration, request, MSKCreateConfigurationResponse)

    async def create_replicator(
        self,
        request: MSKCreateReplicatorRequest,
    ) -> MSKCreateReplicatorResponse:
        client = self._require_client()
        return await self._execute(client.create_replicator, request, MSKCreateReplicatorResponse)

    async def create_topic(
        self,
        request: MSKCreateTopicRequest,
    ) -> MSKCreateTopicResponse:
        client = self._require_client()
        return await self._execute(client.create_topic, request, MSKCreateTopicResponse)

    async def create_vpc_connection(
        self,
        request: MSKCreateVpcConnectionRequest,
    ) -> MSKCreateVpcConnectionResponse:
        client = self._require_client()
        return await self._execute(client.create_vpc_connection, request, MSKCreateVpcConnectionResponse)

    async def delete_assessment(
        self,
        request: MSKDeleteAssessmentRequest,
    ) -> MSKDeleteAssessmentResponse:
        client = self._require_client()
        return await self._execute(client.delete_assessment, request, MSKDeleteAssessmentResponse)

    async def delete_channel(
        self,
        request: MSKDeleteChannelRequest,
    ) -> MSKDeleteChannelResponse:
        client = self._require_client()
        return await self._execute(client.delete_channel, request, MSKDeleteChannelResponse)

    async def delete_cluster_policy(
        self,
        request: MSKDeleteClusterPolicyRequest,
    ) -> MSKDeleteClusterPolicyResponse:
        client = self._require_client()
        return await self._execute(client.delete_cluster_policy, request, MSKDeleteClusterPolicyResponse)

    async def delete_configuration(
        self,
        request: MSKDeleteConfigurationRequest,
    ) -> MSKDeleteConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.delete_configuration, request, MSKDeleteConfigurationResponse)

    async def delete_replicator(
        self,
        request: MSKDeleteReplicatorRequest,
    ) -> MSKDeleteReplicatorResponse:
        client = self._require_client()
        return await self._execute(client.delete_replicator, request, MSKDeleteReplicatorResponse)

    async def delete_topic(
        self,
        request: MSKDeleteTopicRequest,
    ) -> MSKDeleteTopicResponse:
        client = self._require_client()
        return await self._execute(client.delete_topic, request, MSKDeleteTopicResponse)

    async def delete_vpc_connection(
        self,
        request: MSKDeleteVpcConnectionRequest,
    ) -> MSKDeleteVpcConnectionResponse:
        client = self._require_client()
        return await self._execute(client.delete_vpc_connection, request, MSKDeleteVpcConnectionResponse)

    async def describe_assessment(
        self,
        request: MSKDescribeAssessmentRequest,
    ) -> MSKDescribeAssessmentResponse:
        client = self._require_client()
        return await self._execute(client.describe_assessment, request, MSKDescribeAssessmentResponse)

    async def describe_channel(
        self,
        request: MSKDescribeChannelRequest,
    ) -> MSKDescribeChannelResponse:
        client = self._require_client()
        return await self._execute(client.describe_channel, request, MSKDescribeChannelResponse)

    async def describe_cluster_operation(
        self,
        request: MSKDescribeClusterOperationRequest,
    ) -> MSKDescribeClusterOperationResponse:
        client = self._require_client()
        return await self._execute(client.describe_cluster_operation, request, MSKDescribeClusterOperationResponse)

    async def describe_cluster_operation_v2(
        self,
        request: MSKDescribeClusterOperationV2Request,
    ) -> MSKDescribeClusterOperationV2Response:
        client = self._require_client()
        return await self._execute(client.describe_cluster_operation_v2, request, MSKDescribeClusterOperationV2Response)

    async def describe_configuration_revision(
        self,
        request: MSKDescribeConfigurationRevisionRequest,
    ) -> MSKDescribeConfigurationRevisionResponse:
        client = self._require_client()
        return await self._execute(client.describe_configuration_revision, request, MSKDescribeConfigurationRevisionResponse)

    async def describe_replicator(
        self,
        request: MSKDescribeReplicatorRequest,
    ) -> MSKDescribeReplicatorResponse:
        client = self._require_client()
        return await self._execute(client.describe_replicator, request, MSKDescribeReplicatorResponse)

    async def describe_topic(
        self,
        request: MSKDescribeTopicRequest,
    ) -> MSKDescribeTopicResponse:
        client = self._require_client()
        return await self._execute(client.describe_topic, request, MSKDescribeTopicResponse)

    async def describe_topic_partitions(
        self,
        request: MSKDescribeTopicPartitionsRequest,
    ) -> MSKDescribeTopicPartitionsResponse:
        client = self._require_client()
        return await self._execute(client.describe_topic_partitions, request, MSKDescribeTopicPartitionsResponse)

    async def describe_topic_partitions_paginated(
        self,
        request: MSKDescribeTopicPartitionsRequest,
    ) -> list[MSKDescribeTopicPartitionsResponse]:
        return await self._paginate('describe_topic_partitions', request, MSKDescribeTopicPartitionsResponse)

    async def describe_topic_reassignment(
        self,
        request: MSKDescribeTopicReassignmentRequest,
    ) -> MSKDescribeTopicReassignmentResponse:
        client = self._require_client()
        return await self._execute(client.describe_topic_reassignment, request, MSKDescribeTopicReassignmentResponse)

    async def describe_vpc_connection(
        self,
        request: MSKDescribeVpcConnectionRequest,
    ) -> MSKDescribeVpcConnectionResponse:
        client = self._require_client()
        return await self._execute(client.describe_vpc_connection, request, MSKDescribeVpcConnectionResponse)

    async def get_cluster_policy(
        self,
        request: MSKGetClusterPolicyRequest,
    ) -> MSKGetClusterPolicyResponse:
        client = self._require_client()
        return await self._execute(client.get_cluster_policy, request, MSKGetClusterPolicyResponse)

    async def get_compatible_kafka_versions(
        self,
        request: MSKGetCompatibleKafkaVersionsRequest | None = None,
    ) -> MSKGetCompatibleKafkaVersionsResponse:
        client = self._require_client()
        return await self._execute(client.get_compatible_kafka_versions, request, MSKGetCompatibleKafkaVersionsResponse)

    async def list_assessment_findings(
        self,
        request: MSKListAssessmentFindingsRequest,
    ) -> MSKListAssessmentFindingsResponse:
        client = self._require_client()
        return await self._execute(client.list_assessment_findings, request, MSKListAssessmentFindingsResponse)

    async def list_assessment_findings_paginated(
        self,
        request: MSKListAssessmentFindingsRequest,
    ) -> list[MSKListAssessmentFindingsResponse]:
        return await self._paginate('list_assessment_findings', request, MSKListAssessmentFindingsResponse)

    async def list_assessments(
        self,
        request: MSKListAssessmentsRequest,
    ) -> MSKListAssessmentsResponse:
        client = self._require_client()
        return await self._execute(client.list_assessments, request, MSKListAssessmentsResponse)

    async def list_assessments_paginated(
        self,
        request: MSKListAssessmentsRequest,
    ) -> list[MSKListAssessmentsResponse]:
        return await self._paginate('list_assessments', request, MSKListAssessmentsResponse)

    async def list_channels(
        self,
        request: MSKListChannelsRequest,
    ) -> MSKListChannelsResponse:
        client = self._require_client()
        return await self._execute(client.list_channels, request, MSKListChannelsResponse)

    async def list_client_vpc_connections(
        self,
        request: MSKListClientVpcConnectionsRequest,
    ) -> MSKListClientVpcConnectionsResponse:
        client = self._require_client()
        return await self._execute(client.list_client_vpc_connections, request, MSKListClientVpcConnectionsResponse)

    async def list_client_vpc_connections_paginated(
        self,
        request: MSKListClientVpcConnectionsRequest,
    ) -> list[MSKListClientVpcConnectionsResponse]:
        return await self._paginate('list_client_vpc_connections', request, MSKListClientVpcConnectionsResponse)

    async def list_cluster_operations(
        self,
        request: MSKListClusterOperationsRequest,
    ) -> MSKListClusterOperationsResponse:
        client = self._require_client()
        return await self._execute(client.list_cluster_operations, request, MSKListClusterOperationsResponse)

    async def list_cluster_operations_paginated(
        self,
        request: MSKListClusterOperationsRequest,
    ) -> list[MSKListClusterOperationsResponse]:
        return await self._paginate('list_cluster_operations', request, MSKListClusterOperationsResponse)

    async def list_cluster_operations_v2(
        self,
        request: MSKListClusterOperationsV2Request,
    ) -> MSKListClusterOperationsV2Response:
        client = self._require_client()
        return await self._execute(client.list_cluster_operations_v2, request, MSKListClusterOperationsV2Response)

    async def list_cluster_operations_v2_paginated(
        self,
        request: MSKListClusterOperationsV2Request,
    ) -> list[MSKListClusterOperationsV2Response]:
        return await self._paginate('list_cluster_operations_v2', request, MSKListClusterOperationsV2Response)

    async def list_configuration_revisions(
        self,
        request: MSKListConfigurationRevisionsRequest,
    ) -> MSKListConfigurationRevisionsResponse:
        client = self._require_client()
        return await self._execute(client.list_configuration_revisions, request, MSKListConfigurationRevisionsResponse)

    async def list_configuration_revisions_paginated(
        self,
        request: MSKListConfigurationRevisionsRequest,
    ) -> list[MSKListConfigurationRevisionsResponse]:
        return await self._paginate('list_configuration_revisions', request, MSKListConfigurationRevisionsResponse)

    async def list_kafka_versions(
        self,
        request: MSKListKafkaVersionsRequest | None = None,
    ) -> MSKListKafkaVersionsResponse:
        client = self._require_client()
        return await self._execute(client.list_kafka_versions, request, MSKListKafkaVersionsResponse)

    async def list_kafka_versions_paginated(
        self,
        request: MSKListKafkaVersionsRequest | None = None,
    ) -> list[MSKListKafkaVersionsResponse]:
        return await self._paginate('list_kafka_versions', request, MSKListKafkaVersionsResponse)

    async def list_replicators(
        self,
        request: MSKListReplicatorsRequest | None = None,
    ) -> MSKListReplicatorsResponse:
        client = self._require_client()
        return await self._execute(client.list_replicators, request, MSKListReplicatorsResponse)

    async def list_replicators_paginated(
        self,
        request: MSKListReplicatorsRequest | None = None,
    ) -> list[MSKListReplicatorsResponse]:
        return await self._paginate('list_replicators', request, MSKListReplicatorsResponse)

    async def list_scram_secrets(
        self,
        request: MSKListScramSecretsRequest,
    ) -> MSKListScramSecretsResponse:
        client = self._require_client()
        return await self._execute(client.list_scram_secrets, request, MSKListScramSecretsResponse)

    async def list_scram_secrets_paginated(
        self,
        request: MSKListScramSecretsRequest,
    ) -> list[MSKListScramSecretsResponse]:
        return await self._paginate('list_scram_secrets', request, MSKListScramSecretsResponse)

    async def list_topic_reassignments(
        self,
        request: MSKListTopicReassignmentsRequest,
    ) -> MSKListTopicReassignmentsResponse:
        client = self._require_client()
        return await self._execute(client.list_topic_reassignments, request, MSKListTopicReassignmentsResponse)

    async def list_topic_reassignments_paginated(
        self,
        request: MSKListTopicReassignmentsRequest,
    ) -> list[MSKListTopicReassignmentsResponse]:
        return await self._paginate('list_topic_reassignments', request, MSKListTopicReassignmentsResponse)

    async def list_topics(
        self,
        request: MSKListTopicsRequest,
    ) -> MSKListTopicsResponse:
        client = self._require_client()
        return await self._execute(client.list_topics, request, MSKListTopicsResponse)

    async def list_topics_paginated(
        self,
        request: MSKListTopicsRequest,
    ) -> list[MSKListTopicsResponse]:
        return await self._paginate('list_topics', request, MSKListTopicsResponse)

    async def list_vpc_connections(
        self,
        request: MSKListVpcConnectionsRequest | None = None,
    ) -> MSKListVpcConnectionsResponse:
        client = self._require_client()
        return await self._execute(client.list_vpc_connections, request, MSKListVpcConnectionsResponse)

    async def list_vpc_connections_paginated(
        self,
        request: MSKListVpcConnectionsRequest | None = None,
    ) -> list[MSKListVpcConnectionsResponse]:
        return await self._paginate('list_vpc_connections', request, MSKListVpcConnectionsResponse)

    async def put_cluster_policy(
        self,
        request: MSKPutClusterPolicyRequest,
    ) -> MSKPutClusterPolicyResponse:
        client = self._require_client()
        return await self._execute(client.put_cluster_policy, request, MSKPutClusterPolicyResponse)

    async def reboot_broker(
        self,
        request: MSKRebootBrokerRequest,
    ) -> MSKRebootBrokerResponse:
        client = self._require_client()
        return await self._execute(client.reboot_broker, request, MSKRebootBrokerResponse)

    async def reject_client_vpc_connection(
        self,
        request: MSKRejectClientVpcConnectionRequest,
    ) -> MSKRejectClientVpcConnectionResponse:
        client = self._require_client()
        return await self._execute(client.reject_client_vpc_connection, request, MSKRejectClientVpcConnectionResponse)

    async def start_topic_reassignment(
        self,
        request: MSKStartTopicReassignmentRequest,
    ) -> MSKStartTopicReassignmentResponse:
        client = self._require_client()
        return await self._execute(client.start_topic_reassignment, request, MSKStartTopicReassignmentResponse)

    async def stop_topic_reassignment(
        self,
        request: MSKStopTopicReassignmentRequest,
    ) -> MSKStopTopicReassignmentResponse:
        client = self._require_client()
        return await self._execute(client.stop_topic_reassignment, request, MSKStopTopicReassignmentResponse)

    async def update_broker_count(
        self,
        request: MSKUpdateBrokerCountRequest,
    ) -> MSKUpdateBrokerCountResponse:
        client = self._require_client()
        return await self._execute(client.update_broker_count, request, MSKUpdateBrokerCountResponse)

    async def update_broker_storage(
        self,
        request: MSKUpdateBrokerStorageRequest,
    ) -> MSKUpdateBrokerStorageResponse:
        client = self._require_client()
        return await self._execute(client.update_broker_storage, request, MSKUpdateBrokerStorageResponse)

    async def update_broker_type(
        self,
        request: MSKUpdateBrokerTypeRequest,
    ) -> MSKUpdateBrokerTypeResponse:
        client = self._require_client()
        return await self._execute(client.update_broker_type, request, MSKUpdateBrokerTypeResponse)

    async def update_channel(
        self,
        request: MSKUpdateChannelRequest,
    ) -> MSKUpdateChannelResponse:
        client = self._require_client()
        return await self._execute(client.update_channel, request, MSKUpdateChannelResponse)

    async def update_cluster_configuration(
        self,
        request: MSKUpdateClusterConfigurationRequest,
    ) -> MSKUpdateClusterConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.update_cluster_configuration, request, MSKUpdateClusterConfigurationResponse)

    async def update_cluster_kafka_version(
        self,
        request: MSKUpdateClusterKafkaVersionRequest,
    ) -> MSKUpdateClusterKafkaVersionResponse:
        client = self._require_client()
        return await self._execute(client.update_cluster_kafka_version, request, MSKUpdateClusterKafkaVersionResponse)

    async def update_configuration(
        self,
        request: MSKUpdateConfigurationRequest,
    ) -> MSKUpdateConfigurationResponse:
        client = self._require_client()
        return await self._execute(client.update_configuration, request, MSKUpdateConfigurationResponse)

    async def update_connectivity(
        self,
        request: MSKUpdateConnectivityRequest,
    ) -> MSKUpdateConnectivityResponse:
        client = self._require_client()
        return await self._execute(client.update_connectivity, request, MSKUpdateConnectivityResponse)

    async def update_monitoring(
        self,
        request: MSKUpdateMonitoringRequest,
    ) -> MSKUpdateMonitoringResponse:
        client = self._require_client()
        return await self._execute(client.update_monitoring, request, MSKUpdateMonitoringResponse)

    async def update_rebalancing(
        self,
        request: MSKUpdateRebalancingRequest,
    ) -> MSKUpdateRebalancingResponse:
        client = self._require_client()
        return await self._execute(client.update_rebalancing, request, MSKUpdateRebalancingResponse)

    async def update_replication_info(
        self,
        request: MSKUpdateReplicationInfoRequest,
    ) -> MSKUpdateReplicationInfoResponse:
        client = self._require_client()
        return await self._execute(client.update_replication_info, request, MSKUpdateReplicationInfoResponse)

    async def update_security(
        self,
        request: MSKUpdateSecurityRequest,
    ) -> MSKUpdateSecurityResponse:
        client = self._require_client()
        return await self._execute(client.update_security, request, MSKUpdateSecurityResponse)

    async def update_storage(
        self,
        request: MSKUpdateStorageRequest,
    ) -> MSKUpdateStorageResponse:
        client = self._require_client()
        return await self._execute(client.update_storage, request, MSKUpdateStorageResponse)

    async def update_topic(
        self,
        request: MSKUpdateTopicRequest,
    ) -> MSKUpdateTopicResponse:
        client = self._require_client()
        return await self._execute(client.update_topic, request, MSKUpdateTopicResponse)

