from flet import UserControl, Container, Row,Image,IconButton, Markdown,VerticalDivider,icons,colors,ElevatedButton

class AppBar(UserControl):
    def build(self):

        return Container(
            height=50,
            content=Row(
                controls=[
                Image(src='assets/images/logo.png',expand=True), # imagem do gelc
                Markdown("# Editor de MD"), # o título do programa
                Container(expand=True), # expande o open_pop_savecontainer

                VerticalDivider(),
                IconButton(
                    icon=icons.CLOSE,
                    icon_size=25,
                    hover_color=colors.TEAL_100,
                    tooltip="Fechar",
                    on_click=lambda _: self.page.window_close()
                ),

                ]
            )
        )

class ButtonSave(UserControl):
    def build(self):
        return ElevatedButton(
            text="Save",
            bgcolor=colors.GREEN_400,
            color=colors.WHITE,
        )