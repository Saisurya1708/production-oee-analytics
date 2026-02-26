# OEE Methodology

Overall Equipment Effectiveness (OEE) is a key metric in lean manufacturing that combines three factors—Availability, Performance and Quality—to measure how effectively a machine or line is utilized.

## Availability

Availability measures the percentage of scheduled time that the equipment is available to operate. It is calculated as:

```
Availability = (Scheduled Time – Unplanned Downtime) / Scheduled Time
```

Scheduled time is the total time the equipment is expected to run. Unplanned downtime includes breakdowns and other unexpected stops.

## Performance

Performance compares the actual production rate to the ideal rate. It accounts for speed losses such as minor stops and reduced speed.

```
Performance = (Total Units Produced × Ideal Cycle Time) / Operating Time
```

Ideal cycle time is the fastest time to produce one unit. Operating time is the scheduled time minus unplanned downtime.

## Quality

Quality measures the proportion of good units produced versus total units produced. It reflects scrap and rework.

```
Quality = Good Units Produced / Total Units Produced
```

## Overall Equipment Effectiveness

OEE is the product of the three factors:

```
OEE = Availability × Performance × Quality
```

Expressed as a percentage, OEE provides a holistic view of manufacturing efficiency. Improving any of the three components will increase OEE.

For more information on how OEE is calculated in this toolkit, see the implementation in `src/oee/analysis.py` and the accompanying documentation in the `docs` directory.
