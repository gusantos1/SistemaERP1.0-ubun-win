import sys
import json
import sqlite3
from login import *
from principal import *
from cadastro import *
from entrada import *
from saida import *
from venda import *
from editar import *
from historico import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from datetime import datetime
from random import randint
from functools import partial

usuario = ''


class JanelaLogin(QMainWindow, Ui_JanelaLogin):
    def __init__(self):
        super().__init__(parent=None)
        super().setupUi(self)
        self.btn_entrar.clicked.connect(self.entrar)
        self.btn_fechar_alert.clicked.connect(lambda: self.fr_alert.hide())
        self.fr_alert.hide()


    def entrar(self):
        try:
            login = self.le_login.text()
            senha = self.le_senha.text()
            self.banco = sqlite3.connect('base_login.db')
            self.cursor = self.banco.cursor()
            self.cursor.execute(f"SELECT senha, nome FROM acessos WHERE login = '{login}'")
            dados = self.cursor.fetchall()
            if len(list(dados)) == 0:
                self.fr_alert.show()
                self.lb_erro.setText('Usuário não identificado.')
                self.lb_erro.setStyleSheet("font-size: 16px")
            else:
                self.senha_bd = dados[0][0]
                if senha == self.senha_bd:
                    global usuario
                    usuario =''.join(dados[0][1])
                    self.app = JanelaPrincipal()
                    self.app.show()
                    self.close()
                else:
                    self.fr_alert.show()
                    self.lb_erro.setText('Senha inválida.')
        except:
            pass
        finally:
            self.cursor.close()
            self.banco.close()


class JanelaPrincipal(QMainWindow, Ui_JanelaPrincipal):
    """Tela principal do projeto que direciona o usuário para as funções do programa."""
    def __init__(self):
        super().__init__(parent=None)
        super().setupUi(self)
        #Cliques
        self.btn_cadastro.clicked.connect(self.tela_cadastro)
        self.btn_entrada.clicked.connect(self.tela_entrada)
        self.btn_saida.clicked.connect(self.tela_saida)
        self.btn_vendas.clicked.connect(self.tela_venda)



        #Instâncias
        self.cadastro = JanelaCadastro()
        self.entrada = JanelaEntrada()
        self.saida = JanelaSaida()
        self.venda = JanelaVenda()
        self.editar = JanelaEditar()
        self.historico = JanelaHistorico()
        self.cadastro.btn_edit_merc.clicked.connect(self.tela_editar)
        self.entrada.btn_log.clicked.connect(partial(self.tela_historico, 'log_entrada'))
        self.saida.btn_log.clicked.connect(partial(self.tela_historico, 'log_saida'))
        self.venda.btn_log.clicked.connect(partial(self.tela_historico, 'log_venda'))


    #Telas
    def tela_cadastro(self):
        self.cadastro.show()
        self.limpa_entradas('cadastro')

    def tela_entrada(self):
        self.entrada.show()
        self.limpa_entradas('entrada')

    def tela_saida(self):
        self.saida.show()
        self.limpa_entradas('saida')

    def tela_venda(self):
        self.venda.show()
        self.limpa_entradas('venda')

    def tela_editar(self):
        self.editar.show()
        self.limpa_entradas('editar')

    def tela_historico(self, log_param):
        self.historico.show()
        self.limpa_entradas('logs', log_param)


    def limpa_entradas(self, tela, log_param=None):
        if tela == 'cadastro':
            self.cadastro.le_produto.clear()
            self.cadastro.le_fornecedor.clear()
            self.cadastro.db_custo.setValue(0.00)
            self.cadastro.db_venda.setValue(0.00)
            self.cadastro.le_status.clear()
            self.cadastro.le_id.clear()
            self.cadastro.cb_departamento.setCurrentIndex(0)

        elif tela == 'entrada':
            self.entrada.lw_entrada.clear()
            self.entrada.le_entrada_id.clear()
            self.entrada.sb_entrada.setValue(0)
            self.entrada.mostrar_mercadorias()

        elif tela == 'saida':
            self.saida.lw_entrada.clear()
            self.saida.le_entrada_id.clear()
            self.saida.sb_entrada.setValue(0)
            self.saida.mostrar_mercadorias()
        elif tela == 'venda':
            self.venda.lw_entrada.clear()
            self.venda.mostrar_mercadorias()
            self.venda.le_entrada_id.clear()
            self.venda.sb_un_venda.setValue(0)
            self.venda.db_preco_venda.setValue(0.00)
            self.venda.limpa_btn()
            self.venda.db_preco_final.setValue(0.00)
        elif tela == 'editar':
            self.editar.le_produto.clear()
            self.editar.le_fornecedor.clear()
            self.editar.le_status.clear()
            self.editar.db_custo.setValue(0.00)
            self.editar.db_venda.setValue(0.00)
            self.editar.lw_entrada.clear()
            self.editar.mostrar_mercadorias()
        elif tela == 'logs':
            self.historico.lw_entrada.clear()
            if log_param == 'log_entrada':
                self.historico.mostra_log('logs/hist_entrada.log')
                self.historico.lb_nome.setText('HISTÓRICO DE ENTRADA')
            elif log_param == 'log_saida':
                self.historico.mostra_log('logs/hist_saida.log')
                self.historico.lb_nome.setText('HISTÓRICO DE SAÍDA')
            else:
                self.historico.mostra_log('logs/hist_venda.log')
                self.historico.lb_nome.setText('HISTÓRICO DE VENDA')
        else:
            pass


class JanelaCadastro(QMainWindow, Ui_JanelaCadastro):
    """Tela de cadastro para inserção das mercadorias."""
    def __init__(self):
        super().__init__(parent=None)
        super().setupUi(self)
        self.achado = False
        #Connect
        self.salvar.clicked.connect(self.btn_salvar)

    #Method
    def btn_salvar(self):
        """Botão 'SALVAR' da tela de cadastro que trata dos dados de entrada, chamando o método 'verifica'."""
        try:
            self.produto = self.le_produto.text().title()
            self.fornecedor = self.le_fornecedor.text().title()
            self.departamento = self.cb_departamento.currentText().title()
            #criar condição para os preços
            self.custo = self.db_custo.value()
            self.venda = self.db_venda.value()
            if self.venda < self.custo:
                raise QMessageBox.about(self, 'Alerta', 'Preço de venda não pode ser inferior ao de custo.')
            elif self.produto == '' or self.fornecedor == '' or self.departamento == '':
                raise QMessageBox.about(self, 'Alerta', 'Preencha todos os campos corretamente.')
        except Exception:
            self.le_status.setText('ERRO NAS INFORMAÇÕES DO PRODUTO.')
            self.le_status.setStyleSheet("color:red")
        else:
            self.verifica(self.produto, self.fornecedor, self.departamento, self.custo, self.venda)

    def verifica(self, produto, fornecedor, departamento, custo, venda):
        """Função que verifia se as entradas pro cadastro de um produto são válidas."""
        if len(produto) and len(fornecedor) and len(departamento) > 0:
            id = self.gera_id(departamento) #Gera o ID do Produto.

            with open('data/bd.json', 'r+') as bd:
                base = json.load(bd)

            for verif_nome_produto, verif_valores_produto in base['Mercadorias'].items():
                if produto == verif_nome_produto and fornecedor == verif_valores_produto['fornecedor']:
                    self.le_status.setText("Este produto já foi cadastrado.")
                    self.le_status.setStyleSheet("color:red")
                    return
                else:
                    if produto == verif_nome_produto:
                        self.achado = True
                        continue
            else:
                self.id_sorteados[departamento].append(self.digitos)

                with open('data/id_sorteados.json', 'w+') as gravando_id:
                    json.dump(self.id_sorteados, gravando_id, indent=4)
                    mercadoria = {
                            produto +' '+ str(fornecedor) if self.achado else produto:
                            {
                                'id': id,
                                'fornecedor': fornecedor,
                                'departamento': departamento,
                                'preco_de_custo': custo,
                                'preco_de_venda': venda,
                                'quantidade': 0,
                            }
                        }
                    #Cadastrando os produtos
                    base['Mercadorias'].update(mercadoria)
                    with open('data/bd.json', 'w+') as bd:
                        json.dump(base, bd, indent=4)
                    self.le_id.setText(id)
                    self.le_status.setText('CADASTRADO COM SUCESSO.'.rjust(35))
                    self.le_status.setStyleSheet("color:green")

    def gera_id(self, departamento):
        """Função que retorna o ID de um produto com base no id_sorteados.json
        Formato do ID: ano + n° do departamento + 4 digitos aleatórios entre 1000-9999."""
        ano = str(datetime.now().year)
        self.digitos = randint(1000, 9999)

        with open('data/id_sorteados.json', 'r+') as sorteados:
            self.id_sorteados = json.load(sorteados)

        for chave_id, num_sorteados in self.id_sorteados.items():
            while chave_id == departamento and self.digitos in num_sorteados:
                self.digitos = randint(1000, 9999)

        switch = {
                'Utilidades Domésticas': 1,
                'Informática': 2,
                'Eletrodomésticos': 3,
                'Eletroportáteis': 4,
                'Esportivo': 5,
                'Limpeza': 6,
                'Serviços': 7,
                'Outros': 8,
            }
        select = switch.get(departamento)
        return ano + str(select) + str(self.digitos)


class JanelaEditar(QMainWindow, Ui_JanelaEditMerc):
    def __init__(self):
        super().__init__(parent=None)
        super().setupUi(self)
        self.btn_take.clicked.connect(self.tratamento_selecionado)
        self.btn_dialog.button(self.btn_dialog.Save).clicked.connect(self.dialog_salvar)
        self.btn_dialog.button(self.btn_dialog.Cancel).clicked.connect(self.close)
        self.btn_deletar.clicked.connect(self.deletar)

    def deletar(self):
        try:
            self.linha_selecionada = self.lw_entrada.currentRow()
            self.pegar_produto = self.lw_entrada.takeItem(self.linha_selecionada)
            self.lw_entrada.insertItem(self.linha_selecionada, self.pegar_produto)
            self.info_produto = self.pegar_produto.text().split()
            i_produto = self.info_produto.index('Produto:') + 1
            i_fornecedor = self.info_produto.index('Fornecedor:')

            # Nome do produto
            self.nome_produto = []
            for juntando_produto in range(i_produto, i_fornecedor):
                self.nome_produto.append(self.info_produto[juntando_produto])
            self.nome_produto = ' '.join(self.nome_produto)

            with open('data/bd.json', 'r+') as bd:
                base = json.load(bd)
            for achar_produto, valores in base['Mercadorias'].copy().items():
                if self.nome_produto == achar_produto:
                    del base['Mercadorias'][achar_produto]

            with open('data/bd.json', 'w+') as bd:
                json.dump(base, bd, indent=4)
        except:
            pass
        else:
            self.le_status.setText(f'{self.nome_produto} foi deletado. ')
            self.le_status.setStyleSheet("color:green")
        finally:
            self.le_produto.clear()
            self.le_fornecedor.clear()
            self.le_status.clear()
            self.db_custo.setValue(0.00)
            self.db_venda.setValue(0.00)
            self.lw_entrada.clear()
            self.mostrar_mercadorias()

    def dialog_salvar(self):
        try:
            with open('data/bd.json', 'r+') as bd:
                base = json.load(bd)
            produto = self.le_produto.text()
            fornecedor = self.le_fornecedor.text()
            departamento = self.cb_departamento.currentText()
            custo = self.db_custo.value()
            venda = self.db_venda.value()
            if len(produto) > 0 and len(fornecedor) > 0 and len(departamento) > 0:
                if custo > venda:
                    self.le_status.setText('Preço de custo maior que de venda.')
                    self.le_status.setStyleSheet("color:red")
                    raise Tratamento('Preço de custo maior que de venda.')
                else:
                    #Encontrando o produto pelo ID
                    for achar_produto, valores in base['Mercadorias'].copy().items():
                        if self.id in valores['id']:
                            base['Mercadorias'].update({produto: {'id': self.id,
                                                                  'fornecedor': fornecedor,
                                                                  'departamento': departamento,
                                                                  'preco_de_custo': custo,
                                                                  'preco_de_venda': venda,
                                                                  'quantidade': valores['quantidade']}})
                            if produto != achar_produto:
                                del base['Mercadorias'][achar_produto]
            else:
                self.le_status.setText('Preencha todos os campos.')
                self.le_status.setStyleSheet("color:red")
                raise Tratamento('Erro no preenchimento nos campos.')
        except Exception as erro:
            print(erro)
        else:
            with open('data/bd.json', 'w+') as bd:
                json.dump(base, bd, indent=4)
            self.le_status.setText(f'{self.nome_produto} Alterado com sucesso.')
            self.le_status.setStyleSheet("color:green")
        finally:
            self.lw_entrada.clear(), self.mostrar_mercadorias()

    def tratamento_selecionado(self):
        try:
            self.linha_selecionada = self.lw_entrada.currentRow()
            self.pegar_produto = self.lw_entrada.takeItem(self.linha_selecionada)
            self.lw_entrada.insertItem(self.linha_selecionada, self.pegar_produto)
            self.info_produto = self.pegar_produto.text().split()
            i_produto = self.info_produto.index('Produto:') + 1
            i_fornecedor = self.info_produto.index('Fornecedor:')
            i_id = self.info_produto.index('ID:')
            i_custo = self.info_produto.index('Custo:') + 2
            i_venda = self.info_produto.index('Venda:') + 2
            self.id = self.info_produto[i_id + 1]

            # Nome do produto
            self.nome_produto = []
            for juntando_produto in range(i_produto, i_fornecedor):
                self.nome_produto.append(self.info_produto[juntando_produto])
            self.nome_produto = ' '.join(self.nome_produto)

            #Nome do fornecedor
            self.nome_fornecedor = []
            for juntando_fornecedor in range(i_fornecedor + 1, i_id):
                self.nome_fornecedor.append(self.info_produto[juntando_fornecedor])
            self.nome_fornecedor = ' '.join(self.nome_fornecedor)

            #Valores
            self.custo = self.info_produto[i_custo]
            self.venda = self.info_produto[i_venda]

            #Preenche le
            self.le_produto.setText(self.nome_produto)
            self.le_fornecedor.setText(self.nome_fornecedor)
            self.db_custo.setValue(float(self.custo))
            self.db_venda.setValue(float(self.venda))
        except Exception as erro:
            print(erro)

    def mostrar_mercadorias(self):
        """Função que importa os dados das mercadorias em arquivo json(bd.json)
        e permite a visualização ao usuário para as operações."""
        with open('data/bd.json', 'r') as bd:
            base = json.load(bd)
            for info_produto in base.values():
                for nome_produto, produto in info_produto.items():
                    item = f'Produto: {nome_produto}{" "*5}' \
                           f'Fornecedor: {produto["fornecedor"]}{" "*5}' \
                           f'ID: {produto["id"]}{" "*5}' \
                           f'Custo: R$ {produto["preco_de_custo"]}{" "*5}' \
                           f'Venda: R$ {produto["preco_de_venda"]}{" "*5}' \
                           f'{produto["departamento"]}'
                    self.lw_entrada.addItem(item)


class JanelaEntrada(QMainWindow, Ui_JanelaEntrada):
    """Tela de entrada que permite ao usuário realizar operações de entrada na quantidade da mercadoria."""
    def __init__(self):
        super().__init__(parent=None)
        super().setupUi(self)
        self.btn_entrar.clicked.connect(partial(self.entrar_mercadoria, True))
        self.lw_entrada.itemSelectionChanged.connect(self.pega_id)

    def mostrar_mercadorias(self):
        """Função que importa os dados das mercadorias em arquivo json(bd.json)
        e permite a visualização ao usuário para as operações."""
        with open('data/bd.json', 'r') as bd:
            base = json.load(bd)
            for info_produto in base.values():
                for nome_produto, produto in info_produto.items():
                    item = f'Produto: {nome_produto}{" "*5}' \
                           f'ID: {produto["id"]}{" "*5}' \
                           f'Quantidade(un): {produto["quantidade"]}'
                    self.lw_entrada.addItem(item)


    def pega_id(self):
        string_in_lista = [item.text() for item in self.lw_entrada.selectedItems()]
        lista_id = ''.join(string_in_lista).split()
        if 'ID:' in lista_id:
            index = lista_id.index('ID:') + 1
            id = lista_id.__getitem__(index)
            self.le_entrada_id.setText(id)
        return ''


    def salva_log(self, msg, file_log):
        timestamp = int(datetime.timestamp(datetime.now()))
        momento = datetime.fromtimestamp(timestamp).strftime('%d/%m/%Y %H:%M:%S')
        with open(file_log, 'a+') as file:
            log = file.write(f'{momento} {msg}\n')


    def entrar_mercadoria(self, entrada=True):
        """Função que trata e realiza as operações de entrada e saída de mercadoria.
        :param entrada True = Operações de entrada
        :param entrada False = Operações de saída."""
        try:
            self.id = self.le_entrada_id.text()
            with open('data/bd.json', 'r+') as bd:
                base = json.load(bd)
            for produto, valor in base['Mercadorias'].items():
                if self.le_entrada_id.text() == valor['id'] and self.sb_entrada.value() > 0:
                    quant_anterior = valor['quantidade']
                    if entrada:
                        base['Mercadorias'][produto]['quantidade'] += self.sb_entrada.value()
                        msg = f"{produto} ({valor['id']}) Entrada: {self.sb_entrada.value()} " \
                              f"({quant_anterior} -> {valor['quantidade']}) {usuario}"
                        self.salva_log(msg, 'logs/hist_entrada.log')
                    else:
                        base['Mercadorias'][produto]['quantidade'] -= self.sb_entrada.value()
                        msg = f"{produto} ({valor['id']}) Saída: {self.sb_entrada.value()} " \
                              f"({quant_anterior} -> {valor['quantidade']}) {usuario}"
                        self.salva_log(msg, 'logs/hist_saida.log')
            if self.le_entrada_id.text() == "":
                return QMessageBox.about(self, "Alerta", "Preencha o campo ID.")
            elif self.sb_entrada.value() == 0:
                return QMessageBox.about(self, "Alerta", "Não foi possível realizar entrada de mercadoria.\n")\
                    if entrada else QMessageBox.about(self, "Alerta", "Não foi possível realizar saída de mercadoria.\n")
            elif self.le_entrada_id.text() not in [ids['id'] for ids in base['Mercadorias'].values()]:
                return QMessageBox.about(self, "Alerta", "Essa mercadoria não existe.")
            else:
                pass
        except Exception as erro:
            print(erro)
        else:
            with open('data/bd.json', 'w+') as bd:
                json.dump(base, bd, indent=4)
            return QMessageBox.about(self, "Entrada de Mercadoria", "Entrada com sucesso.") \
                if entrada else QMessageBox.about(self, "Saída de Mercadoria", "Saída com sucesso.")
        finally:
            return self.lw_entrada.clear(), self.mostrar_mercadorias()


class JanelaHistorico(QMainWindow, Ui_JanelaHistorico):
    def __init__(self):
        super().__init__(parent=None)
        super().setupUi(self)

    def mostra_log(self, file_log):
        with open(f'{file_log}', 'r') as bd:
            for mostra in bd.readlines():
                self.lw_entrada.addItem(mostra)


class JanelaSaida(Ui_JanelaSaida, JanelaEntrada):
    """Tela de saída que permite ao usuário realizar operações de saída na quantidade da mercadoria."""
    def __init__(self):
        super(JanelaEntrada, self).__init__(parent=None)
        super(JanelaSaida, self).setupUi(self)
        self.btn_sair.clicked.connect(partial(self.entrar_mercadoria, False))
        self.lw_entrada.itemSelectionChanged.connect(self.pega_id)


class JanelaVenda(QMainWindow, Ui_JanelaVenda):
    def __init__(self):
        super().__init__(parent=None)
        super().setupUi(self)
        self.btn_venda.clicked.connect(self.vender)
        self.btn_limpar.clicked.connect(self.limpa_btn)
        self.lw_entrada.itemSelectionChanged.connect(self.pega_id_pvenda)
        self.instanceEnt = JanelaEntrada()
        self.log_venda = self.instanceEnt.salva_log

    def pega_id_pvenda(self):
        string_in_lista = [item.text() for item in self.lw_entrada.selectedItems()]
        lista_id = ''.join(string_in_lista).split()
        if 'ID:' in lista_id:
            index = lista_id.index('ID:') + 1
            id = lista_id.__getitem__(index)
            self.le_entrada_id.setText(id)

            index_venda = lista_id.index('venda') + 2
            venda = lista_id.__getitem__(index_venda)
            self.db_preco_venda.setValue(float(venda))
        return ''

    def mostrar_mercadorias(self):
        """Função que importa os dados das mercadorias em arquivo json(bd.json) e
        permite a visualização ao usuário para as operações."""
        with open('data/bd.json', 'r') as bd:
            base = json.load(bd)
            for info_produto in base.values():
                for nome_produto, produto in info_produto.items():
                    item = f'Produto: {nome_produto}{" "*20}' \
                           f'ID: {produto["id"]}{" "*10}' \
                           f'Quantidade(un): {produto["quantidade"]}{" "*15}' \
                           f'Preço de custo R$: {produto["preco_de_custo"]}{" "*20}' \
                           f'Preço de venda R$: {produto["preco_de_venda"]}{" "*20}'
                    self.lw_entrada.addItem(item)

    def limpa_btn(self):
        #Limpa botão Aumento
        self.rb_aum.setAutoExclusive(False)
        self.rb_aum.setChecked(False)
        self.rb_aum.setAutoExclusive(True)
        #Limpa botão Desconto
        self.rb_desc.setAutoExclusive(False)
        self.rb_desc.setChecked(False)
        self.rb_desc.setAutoExclusive(True)
        #Limpa botão Porcento
        self.dsb_porcent.setValue(0.0)

    def vender(self):
        try:
            self.id = self.le_entrada_id.text()
            self.preco = self.db_preco_venda.value()
            self.porcent = self.dsb_porcent.value() / 100

            if self.rb_aum.isChecked() or self.rb_desc.isChecked():
                if self.rb_aum.isChecked():
                    self.pfinal = self.preco*(1+self.porcent)
                else:
                    self.pfinal = self.preco*(1-self.porcent)
                self.db_preco_final.setValue(self.pfinal*self.sb_un_venda.value())
            else:
                self.db_preco_final.setValue(self.preco*self.sb_un_venda.value())
            with open('data/bd.json', 'r+') as bd:
                base = json.load(bd)
            for produto, valor in base['Mercadorias'].items():
                if self.id == "":
                    return QMessageBox.about(self, "Alerta", "Preencha o campo ID.")
                elif self.id not in [ids['id'] for ids in base['Mercadorias'].values()]:
                    return QMessageBox.about(self, "Alerta", "Essa mercadoria não existe.")
                else:
                    if self.id == valor['id']:
                        if self.db_preco_final.value() >= valor['preco_de_custo'] and \
                                0 < self.sb_un_venda.value() <= valor['quantidade']:
                            quant_anterior = valor['quantidade']
                            base['Mercadorias'][produto]['quantidade'] -= int(self.sb_un_venda.value())
                            msg = f"{produto} ({valor['id']}) Venda: {self.sb_un_venda.value()} " \
                                  f"({quant_anterior} -> {valor['quantidade']}) " \
                                  f"R$ {self.db_preco_final.value()} {usuario}"
                            self.log_venda(msg, 'logs/hist_venda.log')
                            QMessageBox.about(self, "Venda de Mercadoria", "Venda realizada com sucesso.")
                        else:
                            if self.sb_un_venda.value() == 0:
                                QMessageBox.about(self, "Alerta", "Insira uma quantidade válida.")
                            elif self.db_preco_final.value() < valor['preco_de_custo']:
                                QMessageBox.about(self, "Alerta", "Preço inferior ao mínimo de custo.")
                            else:
                                QMessageBox.about(self, "Alerta", "Quantidade inferior disponível no estoque.")

        except Exception as erro:
            print(erro)
        else:
            with open('data/bd.json', 'w+') as bd:
                json.dump(base, bd, indent=4)
        finally:
            return self.lw_entrada.clear(), self.mostrar_mercadorias()


class Tratamento(Exception):
    pass


def main():

    app = QApplication(sys.argv)
    ex = JanelaLogin()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()