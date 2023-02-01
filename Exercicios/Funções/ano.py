def readable_datetime(dias):
    anos = dias // 365
    resto_anos = dias % 365
    meses = resto_anos // 30
    resto_meses = resto_anos % 30
    semanas = resto_meses // 7
    resto = resto_meses % 7
    return {'anos': anos, 'meses': meses, 'semanas': semanas, 'dias': resto}


print(readable_datetime(400))


