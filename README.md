##### Results of the experiments

| Approach | R² | RMSE | RPD |
|----------|------|--------|------|
| Ridge stacking ensamble | .864 | 5.715 | 2.71 |
| Autogluon ensamble | .853 | 5.938 | 2.61 |
| FCN + SNV + SG + f'(x) | .819 | 6.592 | 2.35 |
| PSLR (two models): splitting for low and high AUC | 0.812 | 6.712 | 2.31 |
| Autogluon ensamble + log(1+x) for y | .806 | 6.812 | 2.27 |
| PSLR concated data | .805 | 6.834 | 2.26 |
| PSLR (59c) + log(1+x) for y | .769 | 7.441 | 2.08 |
| PSLR (29c) + SNV + SG + f'(x) | .787 | 7.138 | 2.17 |
| PSLR (two models) + SNV + SG + f'(x): splitting for low and high AUC | 0.769 | 7.123 | 2.08 |
| SVR + SNV + SG + f'(x) | .75 | 7.649 | 2.02 |
| PSLR baseline (51c) | .738 | 7.926 | 1.95 |
| SVR + SNV + SG + f'(x) + log(1+x) for y | .721 | 8.18 | 1.89 |
| SVR | 0.595 | 9.854 | 1.57 |
| PSLR (37c) + SNV + SG + f'(x) + log(1+x) for y | .802 | 18.922 | 0.82 |