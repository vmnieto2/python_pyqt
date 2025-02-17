import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, 
    QTextEdit, QTableWidget, QTableWidgetItem, QFrame, QMessageBox, QSizePolicy
)
from PyQt5.QtGui import QIcon
import re

class Formulario(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Sistema de Registro')

        # Establecer el icono
        self.setWindowIcon(QIcon('luigi.jpg'))

        main_layout = QHBoxLayout()
        left_layout = QVBoxLayout()

        datos = [['Ana', '25', 'ana@test.com', '123456'],
                 ['Luis', '30', 'luis@test.com', '789012'],
                 ['María', '28', 'maria@test.com', '345678'],
                 ['María', '28', 'maria@test.com', '345678'],
                 ['María', '28', 'maria@test.com', '345678'],
                 ['María', '28', 'maria@test.com', '345678'],
                 ['María', '28', 'maria@test.com', '345678'],
                 ['María', '28', 'maria@test.com', '345678'],
                 ['María', '28', 'maria@test.com', '345678'],
                 ['María', '28', 'maria@test.com', '345678'],
                 ['María', '28', 'maria@test.com', '345678'],
                 ['María', '28', 'maria@test.com', '345678'],
                 ]

        # Contenedor 1: Tabla (25% de altura)
        table_frame = QFrame()
        table_frame.setStyleSheet("border: 1px solid gray;")
        self.table = QTableWidget(len(datos), 4)
        self.table.setHorizontalHeaderLabels(['Nombre', 'Edad', 'Correo', 'Teléfono'])
        self.table.setFixedHeight(int(self.screen().size().height() * 0.25))
        self.table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.table.resizeColumnsToContents()
        self.table.setColumnWidth(0, self.table.width() // 4)

        for row, datos_row in enumerate(datos):
            for col, dato in enumerate(datos_row):
                self.table.setItem(row, col, QTableWidgetItem(dato))
        self.table.cellClicked.connect(self.rellenar_formulario)

        left_layout.addWidget(self.table)

        # Contenedor 2: Formulario
        form_frame = QFrame()
        form_frame.setStyleSheet("border: 1px solid gray;")
        form_layout = QVBoxLayout(form_frame)
        self.campos = {}
        for label in ['Nombre', 'Edad', 'Correo', 'Teléfono']:
            form_layout.addWidget(QLabel(label))
            input_field = QLineEdit()
            self.campos[label.lower()] = input_field
            form_layout.addWidget(input_field)
        left_layout.addWidget(form_frame)

        # Contenedor 3: Texto Random
        text_random_frame = QFrame()
        text_random_frame.setStyleSheet("border: 1px solid gray;")
        text_random_layout = QVBoxLayout(text_random_frame)
        text_random_layout.addWidget(QLabel("Texto aleatorio: ¡Bienvenido al sistema!"))
        left_layout.addWidget(text_random_frame)

        # Contenedor 4: Botones decorativos
        buttons_frame = QFrame()
        buttons_frame.setStyleSheet("border: 1px solid gray;")
        buttons_layout = QHBoxLayout(buttons_frame)
        for btn_text in ['Aceptar', 'Cancelar', 'Salir']:
            buttons_layout.addWidget(QPushButton(btn_text))
        left_layout.addWidget(buttons_frame)

        # Agregar el lado derecho: Área de texto
        text_area_frame = QFrame()
        text_area_frame.setStyleSheet("border: 1px solid gray;")
        self.text_area = QTextEdit()
        self.text_area.setPlaceholderText('Detalles aparecerán aquí...')
        text_area_layout = QVBoxLayout(text_area_frame)
        text_area_layout.addWidget(self.text_area)

        main_layout.addLayout(left_layout, 1)
        main_layout.addWidget(text_area_frame, 1)
        self.setLayout(main_layout)
        self.showMaximized()

    def rellenar_formulario(self, row, column):
        for i, campo in enumerate(['nombre', 'edad', 'correo', 'teléfono']):
            valor = self.table.item(row, i).text() if self.table.item(row, i) else ''
            self.campos[campo].setText(valor)
        self.text_area.setText(f"""Seleccionaste:
Nombre: {self.campos['nombre'].text()}
Edad: {self.campos['edad'].text()}
Correo: {self.campos['correo'].text()}
Teléfono: {self.campos['teléfono'].text()}""")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Formulario()
    sys.exit(app.exec_())
