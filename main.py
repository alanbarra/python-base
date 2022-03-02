from cpf_cnpj import Documento
from telefonesBr import TelefonesBr
from datas_br import DatasBr
from acesso_cep import BuscaEndereco

#-------------------------------------------------------
#exemlo_cnpj = "35379838000112"  
#exemlo_cpf = "04964046605"
#documento = Documento.criar_documento(exemlo_cpf)
#print(documento)
#-------------------------------------------------------

#-------------------------------------------------------
#telefone = "55329995930000"
#telefone_objeto = TelefonesBr(telefone)
#print(telefone_objeto)
#-------------------------------------------------------

#-------------------------------------------------------
#cadastro = DatasBr()
#print(cadastro.momento_cadastro)
#print(cadastro.mes_cadastro())
#print(cadastro.dia_semana())
#print(cadastro)
#-------------------------------------------------------

#-------------------------------------------------------
#hoje = DatasBr()
#print(hoje.tempo_cadastro())
#-------------------------------------------------------

cep = 36035250
objeto_cep = BuscaEndereco(cep)
bairro, localidade, uf = objeto_cep.acessa_via_cep()
print(bairro, localidade, uf)



