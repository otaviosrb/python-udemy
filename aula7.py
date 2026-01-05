# and - todas condições devem ser verdadeiras
entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_correta = '12345'
if entrada == 'E' and senha_digitada == senha_correta:
    print('Entrar')
else:
    print('Sair')
