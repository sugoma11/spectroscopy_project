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
| Ridge MSC | .608 | 6.696 | 1.6 |
| SVR | 0.595 | 9.854 | 1.57 |
| PSLR (37c) + SNV + SG + f'(x) + log(1+x) for y | .802 | 18.922 | 0.82 |

##### Appendix: Prediction Plots for Other Approaches

| Method | Plot |
|--------|------|
| SVR (raw X, raw y) | [Figure](https://github.com/sugoma11/spectroscopy_project/blob/main/figures/SVR%20(raw%20X%2C%20raw%20y).png) |
| SVR (processed X, raw y) | [Figure](https://github.com/sugoma11/spectroscopy_project/blob/main/figures/SVR%20(processed%20X%2C%20raw%20y).png) |
| SVR (processed X, log-transformed y) | [Figure](https://github.com/sugoma11/spectroscopy_project/blob/main/figures/SVR%20(processed%20X%2C%20log-transformed%20y).png) |
| PLSR (preprocessed X, log y, 37 components) | [Figure](https://github.com/sugoma11/spectroscopy_project/blob/main/figures/PLSR%20(preprocessed%20X%2C%20log%20y%2C%2037%20components).png) |
| PLSR (concat raw+proc X, log y, 39 components) | [Figure](https://github.com/sugoma11/spectroscopy_project/blob/main/figures/PLSR%20(concat%20raw%2Bproc%20X%2C%20log%20y%2C%2039%20components).png) |
| PLSR (processed X + low + high AUC split), 7 and 26 components | [Figure](https://github.com/sugoma11/spectroscopy_project/blob/main/figures/PLSR%20(processed%20X%20%2B%20low%20%2B%20high%20AUC%20split)%2C%20%0A%207%20and%2026%20components%2C%20respectively.png) |
| Gluon AutoML (raw X, raw y) | [Figure](https://github.com/sugoma11/spectroscopy_project/blob/main/figures/Gluon%20AutoML%20(raw%20X%2C%20raw%20y).png) |
| Gluon AutoML (processed X, log y) | [Figure](https://github.com/sugoma11/spectroscopy_project/blob/main/figures/Gluon%20AutoML%20(processed%20X%2C%20log%20y).png) |
| FCN (Raw Spectra) | [Figure](https://github.com/sugoma11/spectroscopy_project/blob/main/figures/FCN%20(Raw%20Spectra).png) |
| FCN Tuned (Raw Spectra) | [Figure](https://github.com/sugoma11/spectroscopy_project/blob/main/figures/FCN%20Tuned%20(Raw%20Spectra).png) |
| FCN Tuned (SNV + SG1 Preprocessed) | [Figure](https://github.com/sugoma11/spectroscopy_project/blob/main/figures/FCN%20Tuned%20(SNV%20%2B%20SG1%20Preprocessed).png) |