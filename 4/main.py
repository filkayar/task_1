import gen
import edit

M = gen.Gen_Matrix_Int(7, 5, 0, 10)

print("Сгенерированная матрица:")
gen.Print_Matrix_Int(7, M)

print("Отобранный массив:")
m = edit.get_perimeter_elements(M)
gen.Print_Mas_Int(m)

print("Отфильтрованный массив:")
m = edit.remove_zeros(m)
gen.Print_Mas_Int(m)

print(f"Среднее ар. четных элементов: { edit.average_even_elements(m) }")


