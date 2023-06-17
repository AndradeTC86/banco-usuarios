from src.service.service_user import ServiceUser


class TestServiceUser:

    def test_add_user_com_sucesso(self):

        # Setup
        name_add = 'Baiano'
        job_add = 'TechLead'
        resultado_esperado = 'Usuario adicionado com sucesso'
        service = ServiceUser()

        #Chamada
        resultado = service.add_user(name=name_add, job=job_add)

        #Avaliacao
        assert resultado_esperado == resultado


