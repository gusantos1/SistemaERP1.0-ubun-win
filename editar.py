# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editar.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_JanelaEditMerc(object):
    def setupUi(self, JanelaEditMerc):
        JanelaEditMerc.setObjectName("JanelaEditMerc")
        JanelaEditMerc.resize(1200, 462)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(JanelaEditMerc.sizePolicy().hasHeightForWidth())
        JanelaEditMerc.setSizePolicy(sizePolicy)
        JanelaEditMerc.setMinimumSize(QtCore.QSize(1048, 462))
        JanelaEditMerc.setMaximumSize(QtCore.QSize(1200, 462))
        self.centralwidget = QtWidgets.QWidget(JanelaEditMerc)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.le_status = QtWidgets.QLineEdit(self.centralwidget)
        self.le_status.setGeometry(QtCore.QRect(940, 410, 231, 31))
        self.le_status.setDragEnabled(False)
        self.le_status.setReadOnly(True)
        self.le_status.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.le_status.setObjectName("le_status")
        self.btn_deletar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_deletar.setGeometry(QtCore.QRect(840, 400, 81, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_deletar.setFont(font)
        self.btn_deletar.setAutoDefault(False)
        self.btn_deletar.setDefault(False)
        self.btn_deletar.setFlat(False)
        self.btn_deletar.setObjectName("btn_deletar")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(920, 10, 20, 431))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.btn_take = QtWidgets.QPushButton(self.centralwidget)
        self.btn_take.setGeometry(QtCore.QRect(850, 220, 61, 41))
        self.btn_take.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("imgs/row.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_take.setIcon(icon)
        self.btn_take.setIconSize(QtCore.QSize(24, 24))
        self.btn_take.setObjectName("btn_take")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(937, 12, 231, 381))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.le_produto = QtWidgets.QLineEdit(self.layoutWidget)
        self.le_produto.setObjectName("le_produto")
        self.gridLayout.addWidget(self.le_produto, 1, 0, 1, 2)
        self.btn_dialog = QtWidgets.QDialogButtonBox(self.layoutWidget)
        self.btn_dialog.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.btn_dialog.setCenterButtons(True)
        self.btn_dialog.setObjectName("btn_dialog")
        self.gridLayout.addWidget(self.btn_dialog, 8, 0, 1, 2)
        self.lb_departamento = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("C059 [urw]")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lb_departamento.setFont(font)
        self.lb_departamento.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_departamento.setObjectName("lb_departamento")
        self.gridLayout.addWidget(self.lb_departamento, 4, 0, 1, 2)
        self.lb_custo = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("C059 [urw]")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lb_custo.setFont(font)
        self.lb_custo.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_custo.setObjectName("lb_custo")
        self.gridLayout.addWidget(self.lb_custo, 6, 0, 1, 1)
        self.le_fornecedor = QtWidgets.QLineEdit(self.layoutWidget)
        self.le_fornecedor.setObjectName("le_fornecedor")
        self.gridLayout.addWidget(self.le_fornecedor, 3, 0, 1, 2)
        self.lb_fornecedor = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("C059 [urw]")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lb_fornecedor.setFont(font)
        self.lb_fornecedor.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_fornecedor.setObjectName("lb_fornecedor")
        self.gridLayout.addWidget(self.lb_fornecedor, 2, 0, 1, 2)
        self.cb_departamento = QtWidgets.QComboBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cb_departamento.setFont(font)
        self.cb_departamento.setObjectName("cb_departamento")
        self.cb_departamento.addItem("")
        self.cb_departamento.setItemText(0, "")
        self.cb_departamento.addItem("")
        self.cb_departamento.addItem("")
        self.cb_departamento.addItem("")
        self.cb_departamento.addItem("")
        self.cb_departamento.addItem("")
        self.cb_departamento.addItem("")
        self.cb_departamento.addItem("")
        self.cb_departamento.addItem("")
        self.gridLayout.addWidget(self.cb_departamento, 5, 0, 1, 2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.db_custo = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.db_custo.setAlignment(QtCore.Qt.AlignCenter)
        self.db_custo.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.db_custo.setAccelerated(True)
        self.db_custo.setKeyboardTracking(True)
        self.db_custo.setProperty("showGroupSeparator", False)
        self.db_custo.setDecimals(2)
        self.db_custo.setMaximum(99999990.0)
        self.db_custo.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.db_custo.setObjectName("db_custo")
        self.horizontalLayout.addWidget(self.db_custo)
        self.db_venda = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.db_venda.setAlignment(QtCore.Qt.AlignCenter)
        self.db_venda.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.db_venda.setAccelerated(True)
        self.db_venda.setKeyboardTracking(True)
        self.db_venda.setProperty("showGroupSeparator", False)
        self.db_venda.setDecimals(2)
        self.db_venda.setMaximum(99999990.0)
        self.db_venda.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.db_venda.setObjectName("db_venda")
        self.horizontalLayout.addWidget(self.db_venda)
        self.gridLayout.addLayout(self.horizontalLayout, 7, 0, 1, 2)
        self.lb_venda = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("C059 [urw]")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lb_venda.setFont(font)
        self.lb_venda.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_venda.setObjectName("lb_venda")
        self.gridLayout.addWidget(self.lb_venda, 6, 1, 1, 1)
        self.lb_produto = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("C059 [urw]")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lb_produto.setFont(font)
        self.lb_produto.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_produto.setObjectName("lb_produto")
        self.gridLayout.addWidget(self.lb_produto, 0, 0, 1, 2)
        self.lw_entrada = QtWidgets.QListWidget(self.centralwidget)
        self.lw_entrada.setGeometry(QtCore.QRect(20, 10, 801, 431))
        self.lw_entrada.setObjectName("lw_entrada")
        JanelaEditMerc.setCentralWidget(self.centralwidget)

        self.retranslateUi(JanelaEditMerc)
        QtCore.QMetaObject.connectSlotsByName(JanelaEditMerc)

    def retranslateUi(self, JanelaEditMerc):
        _translate = QtCore.QCoreApplication.translate
        JanelaEditMerc.setWindowTitle(_translate("JanelaEditMerc", "EDITAR MERCADORIA"))
        self.btn_deletar.setText(_translate("JanelaEditMerc", "DELETAR"))
        self.lb_departamento.setText(_translate("JanelaEditMerc", "Departamento"))
        self.lb_custo.setText(_translate("JanelaEditMerc", "<html><head/><body><p><span style=\" font-size:10pt;\">  Custo R$</span></p></body></html>"))
        self.lb_fornecedor.setText(_translate("JanelaEditMerc", "Fornecedor"))
        self.cb_departamento.setItemText(1, _translate("JanelaEditMerc", "Utilidades Domésticas"))
        self.cb_departamento.setItemText(2, _translate("JanelaEditMerc", "Informática"))
        self.cb_departamento.setItemText(3, _translate("JanelaEditMerc", "Eletrodomésticos"))
        self.cb_departamento.setItemText(4, _translate("JanelaEditMerc", "Eletroportáteis"))
        self.cb_departamento.setItemText(5, _translate("JanelaEditMerc", "Esportivo"))
        self.cb_departamento.setItemText(6, _translate("JanelaEditMerc", "Limpeza"))
        self.cb_departamento.setItemText(7, _translate("JanelaEditMerc", "Serviços"))
        self.cb_departamento.setItemText(8, _translate("JanelaEditMerc", "Outros"))
        self.lb_venda.setText(_translate("JanelaEditMerc", "<html><head/><body><p><span style=\" font-size:10pt;\">Venda R$</span></p></body></html>"))
        self.lb_produto.setText(_translate("JanelaEditMerc", "Produto"))
