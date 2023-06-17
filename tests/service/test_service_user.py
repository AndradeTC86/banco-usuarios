from src.service.service_user import ServiceUser


class TestServiceUser:

    def test_add_user_com_sucesso(self):
        # Setup
        name_add = 'Leonardo'
        job_add = 'TechLead'
        resultado_esperado = 'Usuario adicionado com sucesso'
        service = ServiceUser()

        # Chamada
        resultado = service.add_user(name=name_add, job=job_add)

        # Avaliacao
        assert resultado_esperado == resultado

    def test_validate_existing_user(self):
        # Setup
        name_rep = 'Thiago'
        job_rep = 'Tester'
        resultado_esperado = 'Usuario ja cadastrado'
        service = ServiceUser()

        # Chamada
        resultado = service.add_user(name=name_rep, job=job_rep)

        # Avaliacao
        assert resultado_esperado == resultado

    def test_validate_null_user(self):
        # Setup
        name_null = None
        job_null = 'Tester'
        resultado_esperado = 'Usuario nao adicionado'
        service = ServiceUser()

        # Chamada
        resultado = service.add_user(name=name_null, job=job_null)

        # Avaliacao
        assert resultado_esperado == resultado

    def test_validate_invalid_user(self):
        # Setup
        name_inv = 100
        job_inv = 'Tester'
        resultado_esperado = 'Nome ou Profissao precisa ser um texto'
        service = ServiceUser()

        # Chamada
        resultado = service.add_user(name=name_inv, job=job_inv)

        # Avaliacao
        assert resultado_esperado == resultado

    def test_validate_invalid_job(self):
        # Setup
        name_inv = 'Matheus'
        job_inv = 100
        resultado_esperado = 'Nome ou Profissao precisa ser um texto'
        service = ServiceUser()

        # Chamada
        resultado = service.add_user(name=name_inv, job=job_inv)

        # Avaliacao
        assert resultado_esperado == resultado
