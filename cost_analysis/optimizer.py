"""
Cost Optimizer
This module analyzes cloud resource usage and recommends cost-saving measures.
"""
import pandas as pd

class CostOptimizer:
    """
    Analyzes resource usage data to recommend cost optimization measures.
    
    Attributes:
        usage_data (pd.DataFrame): DataFrame containing resource usage information.
    """
    
    def __init__(self, usage_data: pd.DataFrame):
        self.usage_data = usage_data

    def rightsizing_recommendation(self):
        """
        Provides rightsizing recommendations based on usage patterns.
        
        Returns:
            pd.DataFrame: DataFrame with recommended changes in instance sizes.
        """
        underutilized = self.usage_data[self.usage_data['cpu_usage'] < 20]
        oversized = self.usage_data[self.usage_data['memory_usage'] < 30]
        
        recommendations = pd.concat([underutilized, oversized])
        return recommendations

    def cost_projection(self):
        """
        Projects future cloud costs based on historical data.
        
        Returns:
            float: Projected monthly cost.
        """
        projected_cost = self.usage_data['cost'].mean() * 30
        return projected_cost

if __name__ == "__main__":
    # Example usage
    data = pd.DataFrame({
        'instance_id': ['i-123', 'i-456'],
        'cpu_usage': [10, 80],
        'memory_usage': [15, 90],
        'cost': [5.00, 10.00]
    })
    
    optimizer = CostOptimizer(data)
    print(optimizer.rightsizing_recommendation())
    print(f"Projected Cost: ${optimizer.cost_projection():.2f}")
