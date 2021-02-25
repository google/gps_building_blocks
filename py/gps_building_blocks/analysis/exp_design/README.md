# Experimental media design utils

This directory contains functions that help to design media experiments.

## Install

```bash
pip install gps_building_blocks
```

## A/B Testing Experimental Design Component

This module contains functions that can be used when designing media experiments
to activate Propensity Models built using GA360, Firebase or CRM data. That is,
it estimates different statistical sample sizes required for Test and Control
groups leading to budget and duration estimations based on different expected
uplifts of the conversion rates before starting a media campaign for
remarketing. It is crucial to design media campaigns using these estimations to
make sure the limited experimentation budget is utilized effectively and to set
the right expectations of the campaign outcome.

### Calculate Statistical Sample Size for Proportions

`ab_testing_design.calc_chisquared_sample_size()` estimates the minimum sample
size required for either a Test or a Control group in an A/B test when the KPI
is a proportion such as the conversion rate using the
[Chi-squared test](https://en.wikipedia.org/wiki/Chi-squared_test) of
proportions.

**Usage example:**

```python
from gps_building_blocks.py.analysis.exp_design import ab_testing_design

ab_testing_design.calc_chisquared_sample_size(
    baseline_conversion_rate_percentage=5,
    expected_uplift_percentage=10,
    power_percentage=80,
    confidence_level_percentage=90)
```

**Expected output:** minimum statistical sample size required for either Test or
Control group.

### Calculate Statistical Sample Size for Different Bins of Predicted Probabilities

One way to use the output from a propensity model to optimize marketing is to
first define different audience groups based on the predicted probabilities
(such as `High`, `Medium` and `Low` propensity groups) and then test the same or
different marketing strategies with those.

`ab_testing_design.calc_chisquared_sample_sizes_for_bins()` estimates the
statistical sample sizes required for different groups (bins) of the predicted
probabilities based on different different combinations of the `expected
uplift`, `statistical power` and `confidence levels` specified as parameters by
using the `ab_testing_design.calc_chisquared_sample_size()` function.

**Usage example:**

```python
import numpy as np
from gps_building_blocks.py.analysis.exp_design import ab_testing_design

ab_testing_design.calc_chisquared_sample_sizes_for_bins(
    labels=np.array(prediction_df['label'])
    probability_predictions=np.array(prediction_df['predictions']),
    number_bins=3,
    uplift_percentages=(5, 10, 20),
    power_percentages=(80, 90),
    confidence_level_percentages=(90, 95))
```

**Expected output:** a Pandas dataframe with the following columns containing
statistical sample size for each bin for combination of uplift_percentage,
statistical power and statistical confidence level.

| bin_number | bin_size | conv_rate_percentage | uplift_percentage | power_percentage | confidence_level_percentage | sample_size |
|------------|----------|----------------------|-------------------|------------------|-----------------------------|-------------|
| 1          | 100      | 20                   | 10                | 22               | 20                          | 30          |
| 2          | 200      | 40                   | 15                | 33               | 10                          | 40          |