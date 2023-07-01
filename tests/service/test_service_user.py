from src.service.service_user import ServiceUser


class TestServiceUser:

    def test_add_user_com_sucesso(self):
        name_add = 'Leonardo'
        job_add = 'TechLead'
        resultado_esperado = 'Usuario adicionado com sucesso'
        service = ServiceUser()

        resultado = service.add_user(name=name_add, job=job_add)

        assert resultado_esperado == resultado

    def test_validate_existing_user(self):
        name_rep = 'Thiago'
        job_rep = 'Tester'
        resultado_esperado = 'Usuario ja cadastrado'
        service = ServiceUser()

        resultado = service.add_user(name=name_rep, job=job_rep)

        assert resultado_esperado == resultado

    def test_validate_null_user(self):
        name_null = None
        job_null = 'Tester'
        resultado_esperado = 'Usuario nao adicionado'
        service = ServiceUser()

        resultado = service.add_user(name=name_null, job=job_null)

        assert resultado_esperado == resultado

    def test_validate_null_job(self):
        name_null = 'Matheus'
        job_null = None
        resultado_esperado = 'Usuario nao adicionado'
        service = ServiceUser()

        resultado = service.add_user(name=name_null, job=job_null)

        assert resultado_esperado == resultado

    def test_validate_invalid_user(self):
        name_inv = 100
        job_inv = 'Tester'
        resultado_esperado = 'Nome ou Profissão precisa ser um texto'
        service = ServiceUser()

        resultado = service.add_user(name=name_inv, job=job_inv)

        assert resultado_esperado == resultado

    def test_validate_invalid_job(self):
        name_inv = 'Matheus'
        job_inv = 100
        resultado_esperado = 'Nome ou Profissão precisa ser um texto'
        service = ServiceUser()

        resultado = service.add_user(name=name_inv, job=job_inv)

        assert resultado_esperado == resultado

    def test_delete_user_with_success(self):
        name = 'Thiago'
        resultado_esperado = 'Usuario removido'
        service = ServiceUser()

        resultado = service.del_user(name=name)

        assert resultado_esperado == resultado

    def test_validate_delete_invalid_user(self):
        name = 'Fabricio'
        resultado_esperado = 'Usuario não encontrado'
        service = ServiceUser()

        resultado = service.del_user(name=name)

        assert resultado_esperado == resultado

    def test_validate_delete_null_user(self):
        name = None
        resultado_esperado = 'Usuario não encontrado'
        service = ServiceUser()

        resultado = service.del_user(name=name)

        assert resultado_esperado == resultado

    def test_update_job_with_success(self):
        name = 'Thiago'
        job = 'TechLead'
        resultado_esperado = 'Profissão atualizada com sucesso'
        service = ServiceUser()

        resultado = service.update_user(name=name, new_job=job)

        assert resultado_esperado == resultado

    def test_validate_update_job_invalid_user(self):
        name = 'Fabricio'
        job = 'TechLead'
        resultado_esperado = 'Usuario não encontrado'
        service = ServiceUser()

        resultado = service.update_user(name=name, new_job=job)

        assert resultado_esperado == resultado

    def test_validate_update_job_null_user(self):
        name = None
        job = 'TechLead'
        resultado_esperado = 'Usuario não encontrado'
        service = ServiceUser()

        resultado = service.update_user(name=name, new_job=job)

        assert resultado_esperado == resultado

    def test_select_user_success(self):
        name = 'Thiago'
        resultado_esperado = 'Profissão: Tester'
        service = ServiceUser()

        resultado = service.select_user(name=name)

        assert resultado_esperado == resultado

    def test_validate_select_invalid_user(self):
        name = 'Fabricio'
        resultado_esperado = 'Usuario não encontrado'
        service = ServiceUser()

        resultado = service.select_user(name=name)

        assert resultado_esperado == resultado

    def test_validate_select_null_user(self):
        name = None
        resultado_esperado = 'Usuario não encontrado'
        service = ServiceUser()

        resultado = service.select_user(name=name)

        assert resultado_esperado == resultado
