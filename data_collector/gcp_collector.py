"""
GCP Data Collector
This module collects GCP cloud resource usage using Google Cloud SDK and stores the data for analysis.
"""

import os
from dotenv import load_dotenv
from google.cloud import compute_v1
from google.oauth2 import service_account

# Load environment variables from .env file
load_dotenv()

class GCPDataCollector:
    """
    Collects usage metrics from Google Cloud services using the Google Cloud SDK.
    
    Attributes:
        compute_client (compute_v1.InstancesClient): GCP client for interacting with compute engine instances.
    """
    
    def __init__(self, project_id: str, credentials_file: str):
        credentials = service_account.Credentials.from_service_account_file(credentials_file)
        self.compute_client = compute_v1.InstancesClient(credentials=credentials)
        self.project_id = project_id

    def get_vm_instances(self, zone: str):
        """
        Retrieves virtual machine details including usage metrics from a specific zone.
        
        Parameters:
            zone (str): GCP zone to retrieve instances from.
        
        Returns:
            list: List of VM instances and their details.
        """
        instance_list = self.compute_client.list(project=self.project_id, zone=zone)
        vm_data = []
        
        for instance in instance_list:
            vm_data.append({
                'name': instance.name,
                'zone': zone,
                'machine_type': instance.machine_type
            })
        
        return vm_data

if __name__ == "__main__":
    project_id = os.getenv('GCP_PROJECT_ID')
    credentials_file = os.getenv('GCP_CREDENTIALS')
    gcp_collector = GCPDataCollector(project_id, credentials_file)
    zone = 'us-central1-a'
    vms = gcp_collector.get_vm_instances(zone)
    print(vms)
