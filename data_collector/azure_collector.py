"""
Azure Data Collector
This module collects Azure cloud resource usage using Azure SDK for Python and stores the data for analysis.
"""

import os
from dotenv import load_dotenv
from azure.mgmt.compute import ComputeManagementClient
from azure.identity import DefaultAzureCredential
from datetime import datetime, timedelta

# Load environment variables from .env file
load_dotenv()

class AzureDataCollector:
    """
    Collects usage metrics from Azure services using the Azure SDK.
    
    Attributes:
        compute_client (ComputeManagementClient): Azure compute client for interacting with VMs.
    """
    
    def __init__(self, subscription_id: str):
        self.subscription_id = os.getenv('AZURE_SUBSCRIPTION_ID')
        self.credentials = DefaultAzureCredential()
        self.compute_client = ComputeManagementClient(credential, subscription_id)

    def get_vm_instances(self):
        """
        Retrieves virtual machine details including usage metrics.
        
        Returns:
            list: List of VM instances and their details.
        """
        vm_list = self.compute_client.virtual_machines.list_all()
        vm_data = []
        
        for vm in vm_list:
            vm_data.append({
                'name': vm.name,
                'location': vm.location,
                'vm_size': vm.hardware_profile.vm_size
            })
        
        return vm_data

if __name__ == "__main__":
    subscription_id = 'your-subscription-id'
    azure_collector = AzureDataCollector(subscription_id)
    vms = azure_collector.get_vm_instances()
    print(vms)
