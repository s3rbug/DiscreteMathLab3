import os
import random
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtGui import QFont


def show_message(text: str, message_type=QMessageBox.Warning, title="Увага!"):
    msg = QMessageBox()
    msg.setIcon(message_type)
    msg.setText(text)
    msg.setWindowTitle(title)
    msg.exec_()


def set_to_str(to_convert: set):
    if len(to_convert) == 0:
        return "{}"
    else:
        return str(to_convert)


def can_convert_str_to_int(text: str):
    try:
        int(text)
        return True
    except ValueError:
        return False


def to_set(text: str):
    t = text.replace("{", "").replace("}", "").replace(",", " ")
    t = ' '.join(t.split())
    res = set()
    for i in t.split():
        if not can_convert_str_to_int(i):
            show_message("Перевірте правильність вводу множини!")
            return set()
        res.add(int(i))
    return res


def create_folder():
    if not os.path.exists("logs/"):
        os.mkdir("logs")


def numerate(container):
    return range(len(container))


def print_2d(array):
    for i in array:
        for j in i:
            print(j, end=" ")
        print()
    print()


def bool_chance(chance):
    return random.random() < chance


def center_item(data, font_size=16):
    item = QTableWidgetItem(str(data))
    item.setTextAlignment(Qt.AlignCenter)
    item.setFont(QFont("Lucida Grande", font_size))
    return item
