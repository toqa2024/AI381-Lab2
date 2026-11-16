## Part 4 – Champion Promotion

**Selected model:** Random Forest

**Latency budget:** 25 ms

**Minimum F1 gain:** 0.005

**Reasoning:**

Random Forest achieved the highest F1 score of 0.5289 among the candidates that satisfied the latency budget. Its p95 latency was 23.24 ms, which is below the 25 ms limit.

The previous champion had an F1 score of 0.512. The improvement is 0.0169, exceeding the required minimum gain of 0.005.

I accepted a higher inference latency compared with Logistic Regression in exchange for better F1 performance, while keeping latency within the selected budget.

**Decision:** Promote Random Forest as the new champion.
