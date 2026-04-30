import pytest
from src.utils.calculate import calculate_total

def test_calculate_total():
    # Calling the function with a price of 100.0. 
    # With a default tax_rate of 0.25 (25%), the total should be 125.00
    result = calculate_total(100.0)
    
    # Expected result is 125.00, but function gives 100.0, causing the exact error from your screenshot
    assert result == 125.00
