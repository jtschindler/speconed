
import os
import numpy as np

from matplotlib import pyplot as plt

from speconed import speconed as sod

from pypeit import sampling

def power_law_at_2500(x, amp, slope, z):
    """ Power law model anchored at 2500 AA

    This model is defined for a spectral dispersion axis in Angstroem.

    :param x: Dispersion of the power law
    :type x: np.ndarray
    :param amp: Amplitude of the power law (at 2500 A)
    :type amp: float
    :param slope: Slope of the power law
    :type slope: float
    :param z: Redshift
    :type z: float
    :return: Power law model
    :rtype: np.ndarray

    """

    return amp * (x / (2500. * (z+1.))) ** slope


def test_resample():

    dispersion_a = np.arange(3000, 8000, 5)
    dispersion_b = np.arange(6000, 10000, 11)

    amp = 0.5
    slope = -1.5
    z = 3.0

    flux_den_a = power_law_at_2500(dispersion_a, amp, slope, z)
    flux_den_b = power_law_at_2500(dispersion_b, amp, slope, z)
    fluxden_err_a = np.zeros(dispersion_a.shape)
    fluxden_err_b = np.zeros(dispersion_b.shape)
    sigma_a = np.zeros(dispersion_a.shape)
    for i in range(len(dispersion_a)):
        sigma_a[i] = 0.001  + i/len(dispersion_a) * 0.01
        fluxden_err_a[i] = flux_den_a[i] + np.random.normal(0.0, sigma_a[i])
    sigma_b = np.zeros(dispersion_b.shape)
    for i in range(len(dispersion_b)):
        sigma_b[i] = 0.005  + i/len(dispersion_b) * 0.1
        fluxden_err_b[i] = flux_den_b[i] + np.random.normal(0.0, sigma_b[i])

    # Set up mock spectra with SpecOneD

    s1 = sod.SpecOneD(dispersion=dispersion_a, fluxden=fluxden_err_a,
                      fluxden_err=sigma_a)
    s2 = sod.SpecOneD(dispersion=dispersion_b, fluxden=fluxden_err_b,
                      fluxden_err=sigma_b)



    ov = s2.dispersion[(s2.dispersion > 6000) &  (s2.dispersion < 8000)]
    s_res = s1.resample(ov, force=True)

    res = sampling.Resample(s1.fluxden, e=s1.fluxden_err,
                            x=s1.dispersion, newRange=[6000, 8000],
                            newdx=11, newLog=False)


    from IPython import embed

    embed()

    # plt.plot(dispersion_a, flux_den_a, label='A')
    # plt.plot(dispersion_b, flux_den_b, label='B')
    plt.step(dispersion_a, fluxden_err_a, label='A err', where='mid')
    plt.step(dispersion_b, fluxden_err_b, label='B err', where='mid')
    plt.step(dispersion_a, sigma_a, label='A sigma', where='mid')
    plt.step(dispersion_b, sigma_b, label='B sigma', where='mid')

    plt.step(s_res.dispersion, s_res.fluxden, label='Resampled', where='mid', c='k')
    plt.step(s_res.dispersion, s_res.fluxden_err, label='Resampled err', where='mid', lw=2, c='k')
    plt.step(res.outx, res.outy, label='Resampled PypeIt', where='mid', c='r', lw=2)
    plt.step(res.outx, res.oute, label='Resampled err PypeIt', where='mid', ls=':', lw=2)

    plt.legend()

    plt.show()

if __name__ == '__main__':

    test_resample()

