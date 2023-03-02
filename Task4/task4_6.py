"""
Задание 4.6
Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0
Ограничение: Все задания надо выполнять используя только пройденные темы.
Предупреждение: в разделе 4 тесты можно легко "обмануть" сделав нужный вывод,
без получения результатов из исходных данных с помощью Python.
Это не значит, что задание сделано правильно, просто на данном этапе сложно иначе
проверять результат.
"""

ospf_route = "       10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"

output = "\n{:20} {}" * 5

route = ospf_route.replace(",", " ").replace("[", "").replace("]", "")
route = route.split()

print(output.format(
        "Prefix", route[0],
        "AD/Metric", route[1],
        "Next-Hop", route[3],
        "Last update", route[4],
        "Outbound Interface", route[5],

))