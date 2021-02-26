# coding: utf-8

# Copyright 2019 IBM All Rights Reserved.
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
 This class contains an integration test for the example service.

 Notes:

 1. This example integration test shows how to automatically skip tests if the required config file
    is not available.

 2. Before running this test:
    a. "cp example-service.env.hide example-service.env"
    b. start up the ExampleService service by following the instructions here:
    https://github.ibm.com/CloudEngineering/java-sdk-template/blob/main/README_FIRST.md#integration-tests
"""

import pytest
import unittest
import os
import os.path
import mysdk
from ibm_cloud_sdk_core.authenticators import NoAuthAuthenticator
from ibm_cloud_sdk_core import ApiException
from mysdk.example_service_v1 import *

# Read config file
configFile = 'example-service.env'
configLoaded = None

if os.path.exists(configFile):
    os.environ['IBM_CREDENTIALS_FILE'] = configFile
    configLoaded = True
else:
    print('External configuration was not found, skipping tests...')

class TestExampleServiceV1(unittest.TestCase):
    def setUp(self):
        if not configLoaded:
          self.skipTest("External configuration not available, skipping...")
          
        self.service = mysdk.ExampleServiceV1.new_instance()
        assert self.service is not None

    def tearDown(self):
        # Delete the resources
        print("Clean up complete.")

    def test_1_list_resources(self):
        response = self.service.list_resources()
        assert response is not None
        assert response.get_status_code() == 200
        
        result_dict = response.get_result()
        assert result_dict is not None
        
        result = Resources.from_dict(result_dict)
        assert result is not None
        
        assert result.resources is not None
        assert len(result.resources) >= 2
        
        firstResource = result.resources[0]
        assert firstResource is not None
        assert firstResource.resource_id == "1"
        assert firstResource.name == "The Great Gatsby"
        assert firstResource.tag == "Book"
        
        secondResource = result.resources[1]
        assert secondResource is not None
        assert secondResource.resource_id == "2"
        assert secondResource.name == "Pride and Prejudice"
        assert secondResource.tag == "Book"

    def test_2_get_resource(self):
        response = self.service.get_resource("1")
        assert response is not None
        assert response.get_status_code() == 200
        
        result_dict = response.get_result()
        assert result_dict is not None
        
        result = Resource.from_dict(result_dict)
        assert result is not None
        assert result.resource_id == "1"
        assert result.name == "The Great Gatsby"
        assert result.tag == "Book"
        
    def test_3_get_resource_error(self):
        try:
            response = self.service.get_resource("BAD_RESOURCE_ID")
        except ApiException as e:
            print('Caught expected exception: ', e)
            assert e.code == 404

    def test_4_create_resource(self):
        response = self.service.create_resource(resource_id="3", name="To Kill a Mockingbird", tag="Book")
        assert response is not None
        assert response.get_status_code() == 201
        
        result_dict = response.get_result()
        assert result_dict is not None
        
        result = Resource.from_dict(result_dict)
        print("New Resource: ", result.__str__())
        assert result is not None
        assert result.resource_id == "3"
        assert result.name == "To Kill a Mockingbird"
        assert result.tag == "Book"
