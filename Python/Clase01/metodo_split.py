
#help(str.split)

cursos = 'Java JavaScript Node Python Diseno'
lista_cursos = cursos.split()
print(f'lista de cursos: {lista_cursos}')
print(type(lista_cursos))

#caso 2
cursos_separados_coma = 'Java,Python,Node,JavaScript,Diseño'
lista_cursos = cursos_separados_coma.split(',', 2)
print(f'lista de cursos: {lista_cursos}')
print(len(lista_cursos))