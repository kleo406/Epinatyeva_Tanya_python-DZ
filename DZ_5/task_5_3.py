tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasser = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']


def spisok(tutors, klasser):
    i = 0
    while i < len(tutors) and i < len(klasser):
        yield tutors[i], klasser[i]
        i += 1
    while i > len(tutors):
        yield tutors[i], None
        i += 1
print(*(spisok(tutors, klasser)), sep='\n')
