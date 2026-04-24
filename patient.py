from trytond.model import fields
from trytond.pool import Pool, PoolMeta
from trytond.transaction import Transaction


class Patient(metaclass=PoolMeta):
    __name__ = 'gnuhealth.patient'

    copago_exempt_pregnant = fields.Boolean('Persona embarazada')
    copago_exempt_disabled = fields.Boolean('Persona discapacitada')
    copago_exempt_oncology = fields.Boolean('Paciente oncologico')
    copago_exempt_gynecology = fields.Boolean('Paciente ginecologico')
    copago_exempt_under_one_year = fields.Boolean('Menor a un ano')
    copago_exempt_recent_surgery = fields.Boolean('Cirugia reciente')
    can_manage_copago_exemptions = fields.Function(
        fields.Boolean('Puede gestionar exenciones de copago'),
        'get_can_manage_copago_exemptions')

    @classmethod
    def get_can_manage_copago_exemptions(cls, patients, name):
        if Transaction().user == 0:
            allowed = True
        else:
            ModelData = Pool().get('ir.model.data')
            User = Pool().get('res.user')
            group_id = ModelData.get_id(
                'z_pra_health_patient_copago_exemptions',
                'z_gestor_exepciones')
            user = User(Transaction().user)
            allowed = any(
                group.id == group_id
                for group in user.groups)
        return {patient.id: allowed for patient in patients}
