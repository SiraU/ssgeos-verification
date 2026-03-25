# Independent Verification of SSGEOS conjuntclust6p-2000-2024

An independent statistical review of the claims made in the [SSGEOS conjuntclust6p-2000-2024](https://github.com/ssgeos/conjuntclust6p-2000-2024) repository, which alleges a statistically significant relationship between planetary conjunction clusters and M7.0+ earthquakes.

## Summary of Findings

**The arithmetic is correct. The methodology is not.**

1. **Multiple testing problem.** The study tests thousands of parameter combinations (cluster size, time window, magnitude threshold, center body, time period). A conservative estimate yields 5,250+ possible combinations. The reported p=0.0008 does not survive Bonferroni correction even with as few as 60 tests.

2. **The 1940-2024 extended analysis contradicts the hypothesis.** With M6.5+ earthquakes and a 9-day window, the base probability of at least one earthquake in any random 9-day period is 95.4%. The reported 25/29 matches is actually *below* the expected 27.7. The extended data argues against the claim, not for it.

3. **Conjunction definition is inflated 12.9x.** The multi-centric approach expands 28 classical planet pairs to 360 "conjunctions," dramatically increasing the chance of spurious correlations.

4. **No plausible physical mechanism.** Venus exerts 0.007% of the Moon's tidal force on Earth. Jupiter exerts 0.0007%. If the Moon cannot reliably trigger earthquakes, a body 14,000 times weaker cannot either.

5. **Peer-reviewed research finds no correlation.** Romanet (2023, *Seismica*) systematically tested planetary alignment-earthquake correlations with proper controls and found no significant relationship.

## Requirements

```
pip install scipy numpy
```

## Author

Sira Nur Uysal -- professional classical astrologer and independent researcher.

Previously conducted an empirical study on 3,475 earthquakes (1703-2014) testing all major astrological factors against seismic events. Result: no statistically significant correlation.

## License

MIT
