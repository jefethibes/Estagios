from django.forms import ValidationError
from validate_docbr import CNPJ, CPF
from pycep_correios.exceptions import InvalidCEP
from datetime import date, timedelta


def valida_tamanho_string(nome, campo, tamanho_minimo, tamanho_maximo):
    if len(campo) < tamanho_minimo:
        raise ValidationError('Campo "{}" deve ter no mínimo {} caracteres!!!'.format(nome, tamanho_minimo))
    elif len(campo) > tamanho_maximo:
        raise ValidationError('Campo "{}" deve ter no máximo {} caracteres!!!'.format(nome, tamanho_maximo))
    elif len(campo) == 0:
        raise ValidationError('Campo "{}" obrigatório!!!'.format(nome))
    else:
        return campo


def valida_tamanho_unico(nome, campo, tamanho):
    if len(campo) != tamanho or len(campo) == 0:
        raise ValidationError('{} inválido!!!'.format(nome))
    else:
        return campo


def valida_cpf(cpf):
    validacao = CPF()
    if validacao.validate(cpf) is False:
        raise ValidationError('CPF inválido!!!')
    else:
        return cpf


def valida_cnpj(cnpj):
    validacao = CNPJ()
    if validacao.validate(cnpj) is False:
        raise ValidationError('CNPJ inválido!!!')
    else:
        return cnpj


def valida_cep(cep):
    if InvalidCEP(cep) is False:
        raise ValidationError('CEP inválido!!!')
    else:
        return cep


def valida_matricula(matricula):
    if matricula <= 1000 or matricula > 99999999:
        raise ValidationError('MATRICULA inválida!!!')
    else:
        return matricula


def valida_emails_permitidos(email):
    if '@gmail.com' in email:
        return email
    elif '@hotmail.com' in email:
        return email
    elif '@outlook.com' in email:
        return email
    else:
        raise ValidationError('E-MAIL não permitido!!! São aceitos apenas Gmail, Outlook e Hotmail.')


def valida_valor(valor):
    if valor < 0 or valor > 10000.00:
        raise ValidationError('VALOR inválido!!!')
    else:
        return valor


def valida_data(data):
    if data > date.today() - timedelta(weeks=780) or data < date.today() - timedelta(weeks=6000):
        raise ValidationError('DATA inválida!!!')
    else:
        return data


PAISES = [('Brasil', 'Brasil'), ('Afeganistão', 'Afeganistão'), ('Albânia', 'Albânia'), ('Algéria', 'Algéria'),
          ('Samoa Americana', 'Samoa Americana'), ('Andorra', 'Andorra'), ('Angola', 'Angola'),
          ('Anguilla', 'Anguilla'), ('Antártida', 'Antártida'), ('Antigua e Barbuda', 'Antigua e Barbuda'),
          ('Argentina', 'Argentina'), ('Armênia', 'Armênia'), ('Aruba', 'Aruba'), ('Austrália', 'Austrália'),
          ('Áustria', 'Áustria'), ('Azerbaijão', 'Azerbaijão'), ('Bahamas', 'Bahamas'), ('Bahrein', 'Bahrein'),
          ('Bangladesh', 'Bangladesh'), ('Barbados', 'Barbados'), ('Bielorrússia', 'Bielorrússia'),
          ('Bélgica', 'Bélgica'), ('Belize', 'Belize'), ('Benin', 'Benin'), ('Bermuda', 'Bermuda'), ('Butão', 'Butão'),
          ('Bolívia', 'Bolívia'), ('Bósnia e Herzegovina', 'Bósnia e Herzegovina'), ('Botswana', 'Botswana'),
          ('Ilha Bouvet', 'Ilha Bouvet'),
          ('Território Britânico do Oceano Índico', 'Território Britânico do Oceano Índico'),
          ('Brunei', 'Brunei'), ('Bulgária', 'Bulgária'), ('Burkina Faso', 'Burkina Faso'),
          ('Burundi', 'Burundi'), ('Camboja', 'Camboja'), ('Camarões', 'Camarões'), ('Canadá', 'Canadá'),
          ('Cabo Verde', 'Cabo Verde'), ('Ilhas Cayman', 'Ilhas Cayman'),
          ('República Centro-Africana', 'República Centro-Africana'), ('Chade', 'Chade'), ('Chile', 'Chile'),
          ('China', 'China'), ('Ilha Christmas', 'Ilha Christmas'), ('Ilhas Cocos (Keeling)', 'Ilhas Cocos (Keeling)'),
          ('Colômbia', 'Colômbia'), ('Comores', 'Comores'), ('Congo', 'Congo'), ('Congo (DR)', 'Congo (DR)'),
          ('Ilhas Cook', 'Ilhas Cook'), ('Costa Rica', 'Costa Rica'), ('Costa do Marfim', 'Costa do Marfim'),
          ('Croácia', 'Croácia'), ('Cuba', 'Cuba'), ('Chipre', 'Chipre'), ('República Tcheca', 'República Tcheca'),
          ('Dinamarca', 'Dinamarca'), ('Djibuti', 'Djibuti'), ('Dominica', 'Dominica'),
          ('República Dominicana', 'República Dominicana'), ('Equador', 'Equador'), ('Egito', 'Egito'),
          ('El Salvador', 'El Salvador'), ('Guiné Equatorial', 'Guiné Equatorial'), ('Eritreia', 'Eritreia'),
          ('Estônia', 'Estônia'), ('Etiópia', 'Etiópia'), ('Ilhas Malvinas', 'Ilhas Malvinas'),
          ('Ilhas Faroe', 'Ilhas Faroe'), ('Fiji', 'Fiji'), ('Finlândia', 'Finlândia'), ('França', 'França'),
          ('Guiana Francesa', 'Guiana Francesa'), ('Polinésia Francesa', 'Polinésia Francesa'),
          ('Terras Austrais e Antárticas Francesas', 'Terras Austrais e Antárticas Francesas'),
          ('Gabão', 'Gabão'), ('Gâmbia', 'Gâmbia'), ('Geórgia', 'Geórgia'), ('Alemanha', 'Alemanha'),
          ('Gana', 'Gana'), ('Gibraltar', 'Gibraltar'), ('Grécia', 'Grécia'), ('Groelândia', 'Groelândia'),
          ('Granada', 'Granada'), ('Guadalupe', 'Guadalupe'), ('Guão', 'Guão'), ('Guatemala', 'Guatemala'),
          ('Guiné', 'Guiné'), ('Guiné-Bissau', 'Guiné-Bissau'), ('Guiana', 'Guiana'), ('Haiti', 'Haiti'),
          ('Ilhas Heard e McDonald', 'Ilhas Heard e McDonald'), ('Vaticano', 'Vaticano'), ('Honduras', 'Honduras'),
          ('Hong Kong', 'Hong Kong'), ('Hungria', 'Hungria'), ('Islândia', 'Islândia'), ('Índia', 'Índia'),
          ('Indonésia', 'Indonésia'), ('Iran', 'Iran'), ('Iraque', 'Iraque'), ('Irlanda', 'Irlanda'),
          ('Israel', 'Israel'), ('Itália', 'Itália'), ('Jamaica', 'Jamaica'), ('Japão', 'Japão'),
          ('Jordânia', 'Jordânia'), ('Cazaquistão', 'Cazaquistão'), ('Quênia', 'Quênia'), ('Kiribati', 'Kiribati'),
          ('Coreia do Norte', 'Coreia do Norte'), ('Coreia do Sul', 'Coreia do Sul'), ('Kuwait', 'Kuwait'),
          ('Quirguistão', 'Quirguistão'), ('Laos', 'Laos'), ('Letônia', 'Letônia'), ('Líbano', 'Líbano'),
          ('Lesoto', 'Lesoto'), ('Libéria', 'Libéria'), ('Líbia', 'Líbia'), ('Liechtenstein', 'Liechtenstein'),
          ('Lituânia', 'Lituânia'), ('Luxemburgo', 'Luxemburgo'), ('Macao', 'Macao'), ('Macedônia', 'Macedônia'),
          ('Madagascar', 'Madagascar'), ('Malawi', 'Malawi'), ('Malásia', 'Malásia'), ('Maldivas', 'Maldivas'),
          ('Mali', 'Mali'), ('Malta', 'Malta'), ('Ilhas Marshall', 'Ilhas Marshall'), ('Martinica', 'Martinica'),
          ('Mauritânia', 'Mauritânia'), ('Maurício', 'Maurício'), ('Mayotte', 'Mayotte'), ('México', 'México'),
          ('Micronésia', 'Micronésia'), ('Moldova', 'Moldova'), ('Mônaco', 'Mônaco'), ('Mongólia', 'Mongólia'),
          ('Montserrat', 'Montserrat'), ('Marrocos', 'Marrocos'), ('Moçambique', 'Moçambique'),
          ('Birmânia', 'Birmânia'), ('Namíbia', 'Namíbia'), ('Nauru', 'Nauru'), ('Nepal', 'Nepal'),
          ('Holanda', 'Holanda'), ('Antilhas Holandesas', 'Antilhas Holandesas'), ('Nova Caledônia', 'Nova Caledônia'),
          ('Nova Zelândia', 'Nova Zelândia'), ('Nicarágua', 'Nicarágua'), ('Niger', 'Niger'), ('Nigéria', 'Nigéria'),
          ('Niue', 'Niue'), ('Ilha Norfolk', 'Ilha Norfolk'), ('Ilhas Marianas do Norte', 'Ilhas Marianas do Norte'),
          ('Noruega', 'Noruega'), ('Omã', 'Omã'), ('Paquistão', 'Paquistão'), ('Palau', 'Palau'),
          ('Palestina', 'Palestina'), ('Panamá', 'Panamá'), ('Papua-Nova Guiné', 'Papua-Nova Guiné'),
          ('Paraguai', 'Paraguai'), ('Peru', 'Peru'), ('Filipinas', 'Filipinas'), ('Ilhas Picárnia', 'Ilhas Picárnia'),
          ('Polônia', 'Polônia'), ('Portugal', 'Portugal'), ('Porto Rico', 'Porto Rico'), ('Catar', 'Catar'),
          ('Reunião', 'Reunião'), ('Romênia', 'Romênia'), ('Rússia', 'Rússia'), ('Ruanda', 'Ruanda'),
          ('Santa Helena', 'Santa Helena'), ('São Cristóvão', 'São Cristóvão'), ('Santa Lúcia', 'Santa Lúcia'),
          ('São Pedro e Miquelon', 'São Pedro e Miquelon'), ('São Vicente e Granadinas', 'São Vicente e Granadinas'),
          ('Samoa', 'Samoa'), ('São Marino', 'São Marino'), ('Sao Tomé e Príncipe', 'Sao Tomé e Príncipe'),
          ('Arábia Saudita', 'Arábia Saudita'), ('Senegal', 'Senegal'), ('Sérvia e Montenegro', 'Sérvia e Montenegro'),
          ('Seicheles', 'Seicheles'), ('República da Serra Leoa', 'República da Serra Leoa'),
          ('Singapura', 'Singapura'), ('Eslováquia', 'Eslováquia'), ('Eslovênia', 'Eslovênia'),
          ('Ilhas Salomão', 'Ilhas Salomão'), ('Somália', 'Somália'), ('África do Sul', 'África do Sul'),
          ('Ilhas Geórgia do Sul e Sandwich do Sul', 'Ilhas Geórgia do Sul e Sandwich do Sul'), ('Espanha', 'Espanha'),
          ('Sri Lanka', 'Sri Lanka'), ('Sudão', 'Sudão'), ('Suriname', 'Suriname'), ('Esvalbarde', 'Esvalbarde'),
          ('Suazilândia', 'Suazilândia'), ('Suécia', 'Suécia'), ('Suiça', 'Suiça'), ('Síria', 'Síria'),
          ('Taiwan', 'Taiwan'), ('Tajiquistão', 'Tajiquistão'), ('Tanzânia', 'Tanzânia'), ('Tailândia', 'Tailândia'),
          ('Timor-Leste', 'Timor-Leste'), ('Togo', 'Togo'), ('Toquelau', 'Toquelau'), ('Tonga', 'Tonga'),
          ('Trinidad e Tobago', 'Trinidad e Tobago'), ('Tunísia', 'Tunísia'), ('Turquia', 'Turquia'),
          ('Turcomenistão', 'Turcomenistão'), ('Ilhas Turks e Caicos', 'Ilhas Turks e Caicos'), ('Tuvalu', 'Tuvalu'),
          ('Uganda', 'Uganda'), ('Ucrânia', 'Ucrânia'), ('Emirados Árabes', 'Emirados Árabes'),
          ('Reino Unido', 'Reino Unido'), ('Estados Unidos', 'Estados Unidos'),
          ('Ilhas Menores Distantes dos Estados Unidos', 'Ilhas Menores Distantes dos Estados Unidos'),
          ('Uruguai', 'Uruguai'), ('Uzbequistão', 'Uzbequistão'), ('Vanuatu', 'Vanuatu'), ('Venezuela', 'Venezuela'),
          ('Vietnam', 'Vietnam'), ('Ilhas Virgens Inglesas', 'Ilhas Virgens Inglesas'),
          ('Ilhas Virgens (USA)', 'Ilhas Virgens (USA)'), ('Wallis e Futuna', 'Wallis e Futuna'),
          ('Saara Ocidental', 'Saara Ocidental'), ('Iêmen', 'Iêmen'), ('Zâmbia', 'Zâmbia'), ('Zimbábue', 'Zimbábue')]
