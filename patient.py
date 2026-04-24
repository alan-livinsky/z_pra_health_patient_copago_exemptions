from trytond.model import fields
from trytond.pool import PoolMeta


class Patient(metaclass=PoolMeta):
    __name__ = 'gnuhealth.patient'

    copago_exempt_pregnant = fields.Boolean('Persona embarazada')
    copago_exempt_disabled = fields.Boolean('Persona discapacitada')
    copago_exempt_oncology = fields.Boolean('Paciente oncologico')
    copago_exempt_gynecology = fields.Boolean('Paciente ginecologico')
    copago_exempt_under_one_year = fields.Boolean('Menor a un año')
    copago_exempt_recent_surgery = fields.Boolean('Cirugia reciente')
