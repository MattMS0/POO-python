class Conta:
    def __init__(self, nome="default", saldo=0):
        self.nome = nome
        self.saldo = saldo

    def __str__(self):
        return f"Nome: {self.nome}/ Saldo: {self.saldo}"

    def get_nome(self):
        return self.nome

    def get_saldo(self):
        return self.saldo

    def set_nome(self, novo_nome):
        if type(novo_nome) == str:
            self.nome = novo_nome
            print(f"Nome atualizado para {self.nome}")
        else:
            print("Erro! Nome tem que ser string.")

    def set_saldo(self, novo_saldo):
        if type(novo_saldo) == float or type(novo_saldo) == int:
            self.saldo = novo_saldo
        else:
            print("Erro! Saldo tem que ser float ou int.")

    def deposito(self, valor_deposito):
        if type(valor_deposito) == float or type(valor_deposito) == int:
            self.saldo += valor_deposito
            print(f"Novo saldo: {self.saldo}")
        else:
            print("Erro! Valor tem que ser int ou float!")

    def retirada(self, valor_retirada):
        if type(valor_retirada) == float or type(valor_retirada) == int:
            if self.saldo >= valor_retirada:
                self.saldo -= valor_retirada
                print(f"Novo saldo: {self.saldo}")
            else:
                print("Valor insuficiente!")
        else:
            print("Erro! Valor tem que ser int ou float!")


class PessoaFisica(Conta):
    def __init__(self, nome, saldo, genero='X', cpf=00000000000):
        super().__init__(nome, saldo)
        self.genero = genero
        self.cpf = cpf

    def __str__(self):
        return f"Nome: {self.nome}/ Saldo: {self.saldo}/ Genêro: {self.genero}/ CPF: {self.cpf}"

    def get_genero(self):
        return self.genero

    def get_cpf(self):
        return self.cpf

    def set_genero(self, novo_genero):
        if type(novo_genero) == str:
            self.genero = novo_genero
            print("Genêro atualizado!")
        else:
            print("Erro! Genêro tem que ser string.")

    def set_cpf(self, novo_cpf):
        if type(novo_cpf) == int:
            self.cpf = novo_cpf
            print("Cpf atualizado!")
        else:
            print("Erro! Cpf tem que ser inteiro.")


class PessoaJuridica(Conta):
    def __init__(self, nome, saldo, modalidade="default", cnpj=00000000000000):
        super().__init__(nome, saldo)
        self.modalidade = modalidade
        self.cnpj = cnpj

    def __str__(self):
        return f"Nome: {self.nome}/ Saldo: {self.saldo}" \
               f" Modalidade: {self.modalidade}/ CNPJ: {self.cnpj}"

    def get_modalidade(self):
        return self.modalidade

    def get_cnpj(self):
        return self.cnpj

    def set_modalidade(self, nova_modalidade):
        if type(nova_modalidade) == str:
            self.modalidade = nova_modalidade
            print("Modalidade atualizada!")
        else:
            print("Erro! Modalidade tem que ser string.")

    def set_cnpj(self, novo_cnpj):
        if type(novo_cnpj) == int:
            self.cnpj = novo_cnpj
            print("Cnpj atualizado!")
        else:
            print("Erro! Cnpj tem que ser inteiro.")


if __name__ == "__main__":
    c1 = Conta('Matheus', 1000)
    c2 = Conta()
    pf1 = PessoaFisica("Marianna", 10000, "Feminino", 00000000000)
    pj1 = PessoaJuridica("Pâmela", 20000, 'MEI', 11111111111111)
    print(c1.get_nome())
    print(c1.get_saldo())
    c1.set_saldo(2000)
    c1.set_nome('Lucas')
    print(c1)
    c1.set_saldo("xxx")
    c1.set_nome(1)
    print(pf1)
    print(vars(pf1))
    print(pf1.__dict__)
    print(pj1)
    pf1.deposito(500)
    print(pf1.get_saldo())
    pj1.retirada(2000)
    print(pj1)
    c1.retirada(10000)
    