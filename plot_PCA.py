import PCA as pca
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# data details
dir = "simulated_spectra/"   # data directory
n_PCA_components = [3]
#n_PCA_components = range(1,11)      # number of pca components

wavelims = [(3924,6662)]  #single range
#wavelims = [((4000,4200),(4900,5700))] #multiple subranges in pca

# Main Loop
explained_variances = []
for pcs in n_PCA_components:
    for WL in wavelims:
        X, V, Z, Xs_hat, X_hat, wavelengths, ev = pca.do_PCA(dir, WL, pcs, 1)

        for i in np.arange(0, len(X), 40):
            plt.plot(wavelengths, np.abs(X[i] - X_hat[i]))
            plt.xlim(5500,6000)
            plt.yscale('log')
            plt.xlabel('wavelength')
            plt.ylabel('X - X_hat')
            plt.savefig('images/X%d_pca%d.png'%(i,pcs))
            plt.close()

    explained_variances.append((pcs, ev))

#x, y = list(zip(*explained_variances))
#plt.plot(x, y, 'o')
#plt.yscale('log')
#plt.xlabel('# principal components')
#plt.ylabel('explained variance')
#plt.savefig('images/explained_variances.png')
