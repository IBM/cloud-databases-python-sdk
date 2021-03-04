# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2021.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Integration Tests for CloudDatabasesV5
"""

import os
import pytest
from ibm_cloud_sdk_core import *
from ibm_cloud_databases.cloud_databases_v5 import *

# Config file name
config_file = 'cloud_databases.env'

# Variables to hold link values
task_id_link = None

class TestCloudDatabasesV5():
    """
    Integration Test Class for CloudDatabasesV5
    """

    @classmethod
    def setup_class(cls):
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            cls.cloud_databases_service = CloudDatabasesV5.new_instance(
                )
            assert cls.cloud_databases_service is not None

            cls.config = read_external_sources(
                CloudDatabasesV5.DEFAULT_SERVICE_NAME)
            assert cls.config is not None

        print('Setup complete.')

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    @needscredentials
    def test_add_allowlist_entry(self):

        # Construct a dict representation of a AllowlistEntry model
        allowlist_entry_model = {
            'address': 'testString',
            'description': 'testString'
        }

        add_allowlist_entry_response = self.cloud_databases_service.add_allowlist_entry(
            id='testString',
            ip_address=allowlist_entry_model
        )

        assert add_allowlist_entry_response.get_status_code() == 202
        add_allowlist_entry_response = add_allowlist_entry_response.get_result()
        assert add_allowlist_entry_response is not None

        # Store task_id_link value for later test cases
        global task_id_link
        task_id_link = add_allowlist_entry_response['id']

    @needscredentials
    def test_create_database_user(self):

        # Construct a dict representation of a CreateDatabaseUserRequestUser model
        create_database_user_request_user_model = {
            'user_type': 'database',
            'username': 'james',
            'password': 'kickoutthe'
        }

        create_database_user_response = self.cloud_databases_service.create_database_user(
            id='testString',
            user_type='testString',
            user=create_database_user_request_user_model
        )

        assert create_database_user_response.get_status_code() == 202
        create_database_user_response = create_database_user_response.get_result()
        assert create_database_user_response is not None

        # Store task_id_link value for later test cases
        global task_id_link
        task_id_link = create_database_user_response['id']

    @needscredentials
    def test_delete_allowlist_entry(self):

        delete_allowlist_entry_response = self.cloud_databases_service.delete_allowlist_entry(
            id='testString',
            ipaddress='testString'
        )

        assert delete_allowlist_entry_response.get_status_code() == 202
        delete_allowlist_entry_response = delete_allowlist_entry_response.get_result()
        assert delete_allowlist_entry_response is not None

        # Store task_id_link value for later test cases
        global task_id_link
        task_id_link = delete_allowlist_entry_response['id']

    @needscredentials
    def test_delete_database_user(self):

        delete_database_user_response = self.cloud_databases_service.delete_database_user(
            id='testString',
            user_type='testString',
            username='testString'
        )

        assert delete_database_user_response.get_status_code() == 202
        delete_database_user_response = delete_database_user_response.get_result()
        assert delete_database_user_response is not None

        # Store task_id_link value for later test cases
        global task_id_link
        task_id_link = delete_database_user_response['id']

    @needscredentials
    def test_replace_allowlist(self):

        # Construct a dict representation of a AllowlistEntry model
        allowlist_entry_model = {
            'address': 'testString',
            'description': 'testString'
        }

        replace_allowlist_response = self.cloud_databases_service.replace_allowlist(
            id='testString',
            ip_addresses=[allowlist_entry_model],
            if_match='testString'
        )

        assert replace_allowlist_response.get_status_code() == 202
        replace_allowlist_response = replace_allowlist_response.get_result()
        assert replace_allowlist_response is not None

        # Store task_id_link value for later test cases
        global task_id_link
        task_id_link = replace_allowlist_response['id']

    @needscredentials
    def test_set_deployment_scaling_group(self):

        # Construct a dict representation of a SetMembersGroupMembers model
        set_members_group_members_model = {
            'allocation_count': 4
        }

        # Construct a dict representation of a SetDeploymentScalingGroupRequestSetMembersGroup model
        set_deployment_scaling_group_request_model = {
            'members': set_members_group_members_model
        }

        set_deployment_scaling_group_response = self.cloud_databases_service.set_deployment_scaling_group(
            id='testString',
            group_id='testString',
            set_deployment_scaling_group_request=set_deployment_scaling_group_request_model
        )

        assert set_deployment_scaling_group_response.get_status_code() == 202
        set_deployment_scaling_group_response = set_deployment_scaling_group_response.get_result()
        assert set_deployment_scaling_group_response is not None

        # Store task_id_link value for later test cases
        global task_id_link
        task_id_link = set_deployment_scaling_group_response['id']

    @needscredentials
    def test_list_deployables(self):

        list_deployables_response = self.cloud_databases_service.list_deployables()

        assert list_deployables_response.get_status_code() == 200
        list_deployables_response = list_deployables_response.get_result()
        assert list_deployables_response is not None

    @needscredentials
    def test_list_regions(self):

        list_regions_response = self.cloud_databases_service.list_regions()

        assert list_regions_response.get_status_code() == 200
        list_regions_response = list_regions_response.get_result()
        assert list_regions_response is not None

    @needscredentials
    def test_get_deployment_info(self):

        get_deployment_info_response = self.cloud_databases_service.get_deployment_info(
            id='testString'
        )

        assert get_deployment_info_response.get_status_code() == 200
        get_deployment_info_response = get_deployment_info_response.get_result()
        assert get_deployment_info_response is not None

    @needscredentials
    def test_change_user_password(self):

        # Construct a dict representation of a APasswordSettingUser model
        a_password_setting_user_model = {
            'password': 'xyzzy'
        }

        change_user_password_response = self.cloud_databases_service.change_user_password(
            id='testString',
            user_type='testString',
            username='testString',
            user=a_password_setting_user_model
        )

        assert change_user_password_response.get_status_code() == 200
        change_user_password_response = change_user_password_response.get_result()
        assert change_user_password_response is not None

    @needscredentials
    def test_get_user(self):

        get_user_response = self.cloud_databases_service.get_user(
            id='testString',
            user_id='testString'
        )

        assert get_user_response.get_status_code() == 200
        task = get_user_response.get_result()
        assert task is not None

    @needscredentials
    def test_set_database_configuration(self):

        # Construct a dict representation of a SetConfigurationConfigurationPGConfiguration model
        set_configuration_configuration_model = {
            'max_connections': 115,
            'max_prepared_transactions': 0,
            'deadlock_timeout': 100,
            'effective_io_concurrency': 1,
            'max_replication_slots': 10,
            'max_wal_senders': 12,
            'shared_buffers': 16,
            'synchronous_commit': 'local',
            'wal_level': 'hot_standby',
            'archive_timeout': 300,
            'log_min_duration_statement': 100
        }

        set_database_configuration_response = self.cloud_databases_service.set_database_configuration(
            id='testString',
            configuration=set_configuration_configuration_model
        )

        assert set_database_configuration_response.get_status_code() == 200
        set_database_configuration_response = set_database_configuration_response.get_result()
        assert set_database_configuration_response is not None

    @needscredentials
    def test_get_database_configuration_schema(self):

        get_database_configuration_schema_response = self.cloud_databases_service.get_database_configuration_schema(
            id='testString'
        )

        assert get_database_configuration_schema_response.get_status_code() == 200
        configuration_schema = get_database_configuration_schema_response.get_result()
        assert configuration_schema is not None

    @needscredentials
    def test_list_remotes(self):

        list_remotes_response = self.cloud_databases_service.list_remotes(
            id='testString'
        )

        assert list_remotes_response.get_status_code() == 200
        list_remotes_response = list_remotes_response.get_result()
        assert list_remotes_response is not None

    @needscredentials
    def test_get_remotes_schema(self):

        get_remotes_schema_response = self.cloud_databases_service.get_remotes_schema(
            id='testString'
        )

        assert get_remotes_schema_response.get_status_code() == 200
        get_remotes_schema_response = get_remotes_schema_response.get_result()
        assert get_remotes_schema_response is not None

    @needscredentials
    def test_set_promotion(self):

        # Construct a dict representation of a SetPromotionPromotionPromote model
        set_promotion_promotion_model = {
            'promotion': {}
        }

        set_promotion_response = self.cloud_databases_service.set_promotion(
            id='testString',
            promotion=set_promotion_promotion_model
        )

        assert set_promotion_response.get_status_code() == 200
        set_promotion_response = set_promotion_response.get_result()
        assert set_promotion_response is not None

    @needscredentials
    def test_list_deployment_tasks(self):

        list_deployment_tasks_response = self.cloud_databases_service.list_deployment_tasks(
            id='testString'
        )

        assert list_deployment_tasks_response.get_status_code() == 200
        tasks = list_deployment_tasks_response.get_result()
        assert tasks is not None

    @needscredentials
    def test_get_task(self):

        get_task_response = self.cloud_databases_service.get_task(
            id=task_id_link
        )

        assert get_task_response.get_status_code() == 200
        get_task_response = get_task_response.get_result()
        assert get_task_response is not None

    @needscredentials
    def test_get_backup_info(self):

        get_backup_info_response = self.cloud_databases_service.get_backup_info(
            backup_id='testString'
        )

        assert get_backup_info_response.get_status_code() == 200
        get_backup_info_response = get_backup_info_response.get_result()
        assert get_backup_info_response is not None

    @needscredentials
    def test_list_deployment_backups(self):

        list_deployment_backups_response = self.cloud_databases_service.list_deployment_backups(
            id='testString'
        )

        assert list_deployment_backups_response.get_status_code() == 200
        backups = list_deployment_backups_response.get_result()
        assert backups is not None

    @needscredentials
    def test_start_ondemand_backup(self):

        start_ondemand_backup_response = self.cloud_databases_service.start_ondemand_backup(
            id='testString'
        )

        assert start_ondemand_backup_response.get_status_code() == 200
        start_ondemand_backup_response = start_ondemand_backup_response.get_result()
        assert start_ondemand_backup_response is not None

    @needscredentials
    def test_get_pit_rdata(self):

        get_pit_rdata_response = self.cloud_databases_service.get_pit_rdata(
            id='testString'
        )

        assert get_pit_rdata_response.get_status_code() == 200
        point_in_time_recovery_data = get_pit_rdata_response.get_result()
        assert point_in_time_recovery_data is not None

    @needscredentials
    def test_get_connection(self):

        get_connection_response = self.cloud_databases_service.get_connection(
            id='testString',
            user_type='testString',
            user_id='testString',
            endpoint_type='public',
            certificate_root='testString'
        )

        assert get_connection_response.get_status_code() == 200
        connection = get_connection_response.get_result()
        assert connection is not None

    @needscredentials
    def test_complete_connection(self):

        complete_connection_response = self.cloud_databases_service.complete_connection(
            id='testString',
            user_type='testString',
            user_id='testString',
            endpoint_type='public',
            password='testString',
            certificate_root='testString'
        )

        assert complete_connection_response.get_status_code() == 200
        connection = complete_connection_response.get_result()
        assert connection is not None

    @needscredentials
    def test_list_deployment_scaling_groups(self):

        list_deployment_scaling_groups_response = self.cloud_databases_service.list_deployment_scaling_groups(
            id='testString'
        )

        assert list_deployment_scaling_groups_response.get_status_code() == 200
        groups = list_deployment_scaling_groups_response.get_result()
        assert groups is not None

    @needscredentials
    def test_get_default_scaling_groups(self):

        get_default_scaling_groups_response = self.cloud_databases_service.get_default_scaling_groups(
            type='postgresql'
        )

        assert get_default_scaling_groups_response.get_status_code() == 200
        groups = get_default_scaling_groups_response.get_result()
        assert groups is not None

    @needscredentials
    def test_get_autoscaling_conditions(self):

        get_autoscaling_conditions_response = self.cloud_databases_service.get_autoscaling_conditions(
            id='testString',
            group_id='testString'
        )

        assert get_autoscaling_conditions_response.get_status_code() == 200
        autoscaling_group = get_autoscaling_conditions_response.get_result()
        assert autoscaling_group is not None

    @needscredentials
    def test_set_autoscaling_conditions(self):

        # Construct a dict representation of a AutoscalingDiskGroupDiskScalersCapacity model
        autoscaling_disk_group_disk_scalers_capacity_model = {
            'enabled': True,
            'free_space_less_than_percent': 10
        }

        # Construct a dict representation of a AutoscalingDiskGroupDiskScalersIoUtilization model
        autoscaling_disk_group_disk_scalers_io_utilization_model = {
            'enabled': True,
            'over_period': '30m',
            'above_percent': 45
        }

        # Construct a dict representation of a AutoscalingDiskGroupDiskScalers model
        autoscaling_disk_group_disk_scalers_model = {
            'capacity': autoscaling_disk_group_disk_scalers_capacity_model,
            'io_utilization': autoscaling_disk_group_disk_scalers_io_utilization_model
        }

        # Construct a dict representation of a AutoscalingDiskGroupDiskRate model
        autoscaling_disk_group_disk_rate_model = {
            'increase_percent': 20,
            'period_seconds': 900,
            'limit_mb_per_member': 3670016,
            'units': 'mb'
        }

        # Construct a dict representation of a AutoscalingDiskGroupDisk model
        autoscaling_disk_group_disk_model = {
            'scalers': autoscaling_disk_group_disk_scalers_model,
            'rate': autoscaling_disk_group_disk_rate_model
        }

        # Construct a dict representation of a AutoscalingSetGroupAutoscalingAutoscalingDiskGroup model
        autoscaling_set_group_autoscaling_model = {
            'disk': autoscaling_disk_group_disk_model
        }

        set_autoscaling_conditions_response = self.cloud_databases_service.set_autoscaling_conditions(
            id='testString',
            group_id='testString',
            autoscaling=autoscaling_set_group_autoscaling_model
        )

        assert set_autoscaling_conditions_response.get_status_code() == 200
        set_autoscaling_conditions_response = set_autoscaling_conditions_response.get_result()
        assert set_autoscaling_conditions_response is not None

    @needscredentials
    def test_file_sync(self):

        file_sync_response = self.cloud_databases_service.file_sync(
            id='testString'
        )

        assert file_sync_response.get_status_code() == 200
        file_sync_response = file_sync_response.get_result()
        assert file_sync_response is not None

    @needscredentials
    def test_create_logical_replication_slot(self):

        # Construct a dict representation of a LogicalReplicationSlotLogicalReplicationSlot model
        logical_replication_slot_logical_replication_slot_model = {
            'name': 'customer_replication',
            'database_name': 'customers',
            'plugin_type': 'wal2json'
        }

        create_logical_replication_slot_response = self.cloud_databases_service.create_logical_replication_slot(
            id='testString',
            logical_replication_slot=logical_replication_slot_logical_replication_slot_model
        )

        assert create_logical_replication_slot_response.get_status_code() == 200
        create_logical_replication_slot_response = create_logical_replication_slot_response.get_result()
        assert create_logical_replication_slot_response is not None

    @needscredentials
    def test_get_allowlist(self):

        get_allowlist_response = self.cloud_databases_service.get_allowlist(
            id='testString'
        )

        assert get_allowlist_response.get_status_code() == 200
        allowlist = get_allowlist_response.get_result()
        assert allowlist is not None

    @needscredentials
    def test_kill_connections(self):

        kill_connections_response = self.cloud_databases_service.kill_connections(
            id='testString'
        )

        assert kill_connections_response.get_status_code() == 200
        kill_connections_response = kill_connections_response.get_result()
        assert kill_connections_response is not None

    @needscredentials
    def test_delete_logical_replication_slot(self):

        delete_logical_replication_slot_response = self.cloud_databases_service.delete_logical_replication_slot(
            id='testString',
            name='testString'
        )

        assert delete_logical_replication_slot_response.get_status_code() == 200
        delete_logical_replication_slot_response = delete_logical_replication_slot_response.get_result()
        assert delete_logical_replication_slot_response is not None

    @needscredentials
    def test_delete_database_user(self):

        delete_database_user_response = self.cloud_databases_service.delete_database_user(
            id='testString',
            user_type='testString',
            username='testString'
        )

        assert delete_database_user_response.get_status_code() == 202
        delete_database_user_response = delete_database_user_response.get_result()
        assert delete_database_user_response is not None

        # Store task_id_link value for later test cases
        global task_id_link
        task_id_link = delete_database_user_response['id']

    @needscredentials
    def test_delete_allowlist_entry(self):

        delete_allowlist_entry_response = self.cloud_databases_service.delete_allowlist_entry(
            id='testString',
            ipaddress='testString'
        )

        assert delete_allowlist_entry_response.get_status_code() == 202
        delete_allowlist_entry_response = delete_allowlist_entry_response.get_result()
        assert delete_allowlist_entry_response is not None

        # Store task_id_link value for later test cases
        global task_id_link
        task_id_link = delete_allowlist_entry_response['id']

