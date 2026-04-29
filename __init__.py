from trytond.pool import Pool

from . import patient


def register():
    Pool.register(
        patient.Patient,
        module='z_001_copago_exemptions', type_='model')
