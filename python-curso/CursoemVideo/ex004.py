a = input('Digite algo: ')
print(f'O tipo primitivo de {a} é:', type(a),
      'É minuscula?', a.islower(),
      'É maiuscula?', a.isupper(),
      'É capitalizado?', a.istitle(),
      'É número?',a.isnumeric(),
      'É Alfanúmerico?',a.isalnum())

