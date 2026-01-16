"""Utilities to analyze hourly time-series temperature data.

This module provides a safe `analyze_time_series` function which validates
inputs and either returns a dictionary of summary statistics or raises a
controlled WeatherAnalysisError that callers (for example, Flask handlers)
can catch and show to users.

Behavior notes:
- If `times` or `temperatures` is None or empty -> raise WeatherAnalysisError.
- If lengths mismatch -> function will safely truncate to the shorter length
  and set `truncated` True and add a warning message in the return dict.
- Pairs where either time or temperature is None are skipped; if all pairs
  are invalid after filtering -> raise WeatherAnalysisError.
- Non-numeric temperature values raise WeatherAnalysisError.
"""

import statistics
from typing import Sequence, Any


class WeatherAnalysisError(Exception):
    """Controlled exception raised for invalid or missing inputs."""


def calculate_median(temperatures):
    if not temperatures:
        return None
    return statistics.median(temperatures)


def calculate_standard_deviation(temperatures):
    # statistics.stdev requires at least two data points
    if not temperatures or len(temperatures) < 2:
        return None
    return statistics.stdev(temperatures)


def analyze_time_series(times: Sequence[Any], temperatures: Sequence[Any]):
    """Analyze paired `times` and `temperatures` sequences.

    Args:
        times: sequence of time values (strings or datetimes)
        temperatures: sequence of numeric temperatures (or convertible to float)

    Returns:
        dict with keys: median, stddev, min, min_time, max, max_time, average,
        truncated (bool), warnings (list).

    Raises:
        WeatherAnalysisError: for missing/empty inputs or if no valid pairs exist.

    Notes:
        - If the two sequences have different lengths, the function will analyze
          only up to the shorter length (safe truncation) and include a
          `truncated` flag and `warnings` entry in the returned dict.
        - Pairs with None for time or temperature are skipped; non-numeric
          temperatures raise WeatherAnalysisError.
    """

    if times is None or temperatures is None:
        raise WeatherAnalysisError("Both 'times' and 'temperatures' must be provided.")

    try:
        len_times = len(times)
        len_temps = len(temperatures)
    except TypeError:
        raise WeatherAnalysisError("'times' and 'temperatures' must be sequences (e.g., lists).")

    warnings = []
    truncated = False
    if len_times == 0 or len_temps == 0:
        raise WeatherAnalysisError("'times' and 'temperatures' must not be empty.")

    # If lengths mismatch, we'll truncate to the shorter sequence but document it.
    if len_times != len_temps:
        truncated = True
        warnings.append(f"Input lengths differ: times={len_times}, temperatures={len_temps}; truncated to shorter length.")

    effective_length = min(len_times, len_temps)

    # Build validated pairs: skip pairs where either value is None.
    valid_times = []
    valid_temps = []
    skipped_pairs = 0
    for i in range(effective_length):
        t = times[i]
        temp = temperatures[i]
        if t is None or temp is None:
            skipped_pairs += 1
            continue
        # Ensure temperature is numeric / convertible to float
        try:
            ftemp = float(temp)
        except (TypeError, ValueError):
            raise WeatherAnalysisError(f"Invalid temperature value at index {i}: {temp}")
        valid_times.append(t)
        valid_temps.append(ftemp)

    if skipped_pairs:
        warnings.append(f"Skipped {skipped_pairs} pair(s) where time or temperature was missing.")

    if not valid_temps:
        raise WeatherAnalysisError("No valid time/temperature pairs available after validation.")

    median_temp = calculate_median(valid_temps)
    stddev_temp = calculate_standard_deviation(valid_temps)

    # Safe min/max and corresponding time lookups
    min_temp = min(valid_temps)
    max_temp = max(valid_temps)
    # Use the first occurrence of the min/max
    min_index = valid_temps.index(min_temp)
    max_index = valid_temps.index(max_temp)
    min_temp_time = valid_times[min_index]
    max_temp_time = valid_times[max_index]

    average = sum(valid_temps) / len(valid_temps)

    result = {
        "median": median_temp,
        "stddev": stddev_temp,
        "min": min_temp,
        "min_time": min_temp_time,
        "max": max_temp,
        "max_time": max_temp_time,
        "average": average,
        "truncated": truncated,
        "warnings": warnings,
        # include a small summary of counts for debugging/visibility
        "count": len(valid_temps),
    }

    return result


