A=['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', ]

B = {
    'а': 1,
    'б': 2,
    'в': 3,
    'г': 4,
    'д': 5,
    'е': 6,
    'ё': 7,
    'ж': 8,
    'з': 9,
    'и': 10,
    'й': 11,
    'к': 12,
    'л': 13,
    'м': 14,
    'н': 15,
    'о': 16,
    'п': 17,
    'р': 18,
    'с': 19,
    'т': 20,
    'у': 21,
    'ф': 22,
    'х': 23,
    'ц': 24,
    'ч': 25,
    'ш': 26,
    'щ': 27,
    'ъ': 28,
    'ы': 29,
    'ь': 30,
    'э': 31,
    'ю': 32,
    'я': 33
}


print("Введите слово")
s = str(input())
print("Введите ключ")
k = int(input())
for i in range(len(s)):
    p = B[s[i]]+k
    if p <= 33:
        print(A[B[s[i]]+k], end='')
    else:
        print(A[B[s[i]]+k-33], end='')
