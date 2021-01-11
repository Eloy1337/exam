#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

# Составить программу для решения задачи: Использовать словарь, содержащий следующие ключи: фамилия
# и инициалы; номер группы; успеваемость (список из пяти элементов). Написать программу, выполняющую
# следующие действия: ввод с клавиатуры данных в список, состоящий из словарей заданной структуры; записи
# должны быть упорядочены по алфавиту; вывод на дисплей фамилий и номеров групп для всех студентов, имеющих
# хотя бы одну оценку 2; если таких студентов нет, вывести соответствующее сообщение.

if __name__ == '__main__':
    students = []
    while True:
        command = input(">>> ").lower()
        if command == 'exit':
            break
        elif command == 'add':
            n = 5
            name = input("Введите фамилию и имя: ")
            group = input("Введите группу: ")
            rating = list(map(int, input("Введите пять оценок: ").split(None, n)[:n]))

            for i in rating:
                if i > 5 or i < 2:
                    print("Такой оценки не существует!", file=sys.stderr)
                    exit(1)

            person = {
                'name': name,
                'group': group,
                'rating': rating,
            }

            students.append(person)
            if len(students) > 1:
                students.sort(key=lambda item: item.get('name', ''))
        elif command == 'list':
            line = '+-{}-+-{}-+-{}-+-{}-+-{}-+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 30,
                '-' * 20,
                '-' * 8,
                '-' * 8,
                '-' * 8,
                '-' * 8,
                '-' * 8,
                '-' * 11
            )
            print(line)
            print(
                '| {:^3} | {:^30} | {:^20} | {:^8} | {:^8} | {:^8} | {:^8} | {:^8} |'.format(
                    "№",
                    "Ф.И.О.",
                    "Группа",
                    "1-ая оценка",
                    "2-ая оценка",
                    "3-ая оценка",
                    "4-ая оценка",
                    "5-ая оценка"
                )
            )
            print(line)
            for idx, person in enumerate(students, 1):
                print(
                    '| {:>3} | {:<30} | {:<20} | {:>11} | {:>11} | {:>11} | {:>11} | {:>11} |'.format(
                        idx,
                        person.get('name', ''),
                        person.get('group', ''),
                        person.get('rating[0]', f'{rating[0]}'),
                        person.get('rating[1]', f'{rating[1]}'),
                        person.get('rating[2]', f'{rating[2]}'),
                        person.get('rating[3]', f'{rating[3]}'),
                        person.get('rating[4]', f'{rating[4]}')
                    )
                )
            print(line)
        elif command.startswith('select'):
            count = 0
            for person in students:
                if 2 in rating:
                    count += 1
                    print(
                        '{:>4}: {}'.format(count, person.get('name', ''))
                    )
            if count == 0:
                print("Нет студентов, которые получили оценку - 2.")
        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - добавить студента;")
            print("list - вывести список студентов;")
            print("select <оценка> - найти студентов которые получили такую оценку;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
