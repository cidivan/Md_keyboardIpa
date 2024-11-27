import os
from flet import Page, FloatingActionButton, Row, FontWeight, icons,app,TextButton, ResponsiveRow, Text, TextField, AlertDialog,colors, ElevatedButton
from partials import contentmd
from partials.appbar import AppBar
from partials.keyboardmd import MainKeyboard

# ------------------------------------- Classe do construtor ------------------------------------------#
class App:
    def __init__(self, page:Page):
        super().__init__()
        self.page = page
        self.page.scroll=True
        self.page.bgcolor=colors.GREY_100
        self.page.window_maximized=True
        #self.page.window_title_bar_hidden=True
        self.main()

    def main(self):
        self.appbar = AppBar()
        self.editormd = contentmd.linha_md#EditorMd()
        self.mainkeyboad = MainKeyboard()

        self.page.fonts = {"ipa": "assets/fonts/DoulosSIL-Regular.ttf"}
        # -------------------- popup --------------------------#
        # ========== This function save file ================#
        def save_file_md(e):
            os.makedirs('meus_arquivos_md', exist_ok=True)

            with open(f'meus_arquivos_md/{file_md.value}.md', 'w') as f:
                f.write(contentmd.editor_md.value)
                f.close()
                file_md.value=''
                pop_up_salvar.open = False

             #   self.page.update()
            print(contentmd.editor_md.value)

        # ========== This function close dialogAlert ================#
        def close_popup(e):
            pop_up_salvar.open = False
            self.page.update()

        file_md = TextField(hint_text="Nome do arquivo")

        pop_up_salvar = AlertDialog(
            title=Text(value="Salvar o arquivo"),
            content=Text(value="Digite o nome do arquivo e procure uma pasta com o nome meu_projeto"),
            modal=True,
            actions=[
                file_md,
                Row(controls=[TextButton(text="Cancelar", on_click=close_popup),
                ElevatedButton(text="Salvar", bgcolor=colors.TEAL_300, color=colors.WHITE,
                                  on_click=save_file_md)])
            ]
        )
        #========== This function open dialogAlert ================#
        def open_pop_save(e):
            self.page.dialog = pop_up_salvar
            pop_up_salvar.open = True
            self.page.update()

# ------------------------------------- Layout do programa ------------------------------------------#
        layout = ResponsiveRow(
            spacing=5,
            controls=[
                self.appbar,
                self.editormd,
                Row(wrap=True,
                    controls=[
                        ElevatedButton(
                            icon=icons.CLOSE_SHARP, text="Fechar teclado", tooltip="Fechar o teclado",
                            icon_color=colors.TEAL_500, color=colors.TEAL_500,
                            on_click=lambda e: self.page.remove(self.mainkeyboad)),
                        TextButton(
                            content = Text(
                                value="Exemplo de MD", color=colors.TEAL_500, width=FontWeight.BOLD),
                            tooltip="Exemplo de texto MD",
                            url='https://docs.google.com/document/d/1kfv_jXK3WvH6iOPv7s4ByvYj3eyOYkXDrtnj28f22dc/edit?usp=sharing'),
                        TextButton(
                            content=Text(
                                value="Atividades", color=colors.TEAL_500, width=FontWeight.BOLD),
                            tooltip="Exemplo de texto MD",
                            url='https://drive.google.com/drive/folders/1KDi7WWWv2Y1l-0dWPHFArwhDzlSEtEFo?usp=sharing'),
                        ElevatedButton(
                            icon=icons.KEYBOARD, icon_color=colors.WHITE,
                            bgcolor=colors.TEAL_500, color=colors.WHITE,
                            text= "Teclado",tooltip="Teclado AFI",
                            on_click= lambda e: self.page.add(self.mainkeyboad)),
                    ]
                ),

            ]
        )
# ------------------------------------- Botão flutuante ------------------------------------------#
        self.page.floating_action_button = FloatingActionButton(
            text="Save", tooltip="Enviar o arquivo", autofocus=True,
            bgcolor=colors.TEAL_500,content=Text("Save", color=colors.WHITE),
            on_click=open_pop_save)

        self.page.add(layout)

if __name__=='__main__':
    app(target=App, assets_dir='assets')