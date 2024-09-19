"""
Cost Projection
This module estimates future cloud costs based on historical usage data.
"""

import pandas as pd


class CostProjection:
    """
    Estimates cloud costs based on historical usage data.
    
    Attributes:
        usage_data (pd.DataFrame): DataFrame containing resource usage and cost data.
    """
    
    def __init__(self, usage_data: pd.DataFrame):
        self.usage_data = usage_data

    def project_monthly_cost(self):
        """
        Projects future monthly cloud costs based on historical daily usage.
        
        Returns:
            float: Projected monthly cost based on daily averages.
        """
        if 'cost' in self.usage_data.columns:
            daily_avg = self.usage_data['cost'].mean()
            projected_monthly_cost = daily_avg * 30
            return projected_monthly_cost
        else:
            raise ValueError("Cost data is missing from the usage data")

if __name__ == "__main__":
    # Example usage
    data = pd.DataFrame({
        'instance_id': ['i-123', 'i-456'],
        'cost': [10.00, 15.00]
    })
    
    cost_proj = CostProjection(data)
    print(f"Projected Monthly Cost: ${cost_proj.project_monthly_cost():.2f}")
