from typing import List

def extract_temperatures_from_text(text: str) -> List[float]:
    temperatures = []
    lines = text.split('\n')
    for line in lines:
        parts = line.split(', ')
        if len(parts) == 2:
            temp_str = parts[1].replace('℃', '')
            try:
                temp = float(temp_str)
                temperatures.append(temp)
            except ValueError:
                continue
    return temperatures

def calculate_average_temperature(temperatures: List[float]) -> float:
    if not temperatures:
        return 0.0
    return sum(temperatures) / len(temperatures)

def find_highest_temperature(temperatures: List[float]) -> float:
    if not temperatures:
        return float('-inf')
    return max(temperatures)

def find_lowest_temperature(temperatures: List[float]) -> float:
    if not temperatures:
        return float('inf')
    return min(temperatures)
