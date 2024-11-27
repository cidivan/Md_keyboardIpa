from flet import alignment,Row, UserControl, padding, Container, Text, TextField, colors, icons, ElevatedButton, IconButton, Divider,Column, border_radius, MainAxisAlignment

btns = [
    {'letter': 'p', 'filling': "#089db2", "width":45},
    {'letter': 'b', 'filling': "#089db2", "width":45},
    {'letter': 'e', 'filling': "#049444", "width":45},
    {'letter': 'ɛ', 'filling': "#049444", "width":45},
    {'letter': 'ẽ', 'filling': "#049444", "width":45},
    {'letter': 'ɾ', 'filling': "#089db2", "width":45},{'letter': 'r', 'filling': "#089db2", "width":45},
    {'letter': 't', 'filling': "#089db2", "width":45},{'letter': 'ʧ', 'filling': "#089db2", "width":45},
    {'letter': 'd', 'filling': "#089db2", "width":45},{'letter': 'ʤ', 'filling': "#089db2", "width":45},
    {'letter': 'I', 'filling': "#049444", "width":45},
    {'letter': 'i', 'filling': "#049444", "width":45},
    {'letter': 'ĩ', 'filling': "#049444", "width":45},
    {'letter': 'j', 'filling': "#049444", "width":45},
    {'letter': 'u', 'filling': "#049444", "width":45},{'letter': 'ũ', 'filling': "#049444", "width":45},
    {'letter': 'ʊ', 'filling': "#049444", "width":45},
    {'letter': 'w', 'filling': "#049444", "width":45},
    {'letter': 'ɔ', 'filling': "#049444", "width":45},{'letter': 'o', 'filling': "#049444", "width":45},{'letter': 'õ', 'filling': "#049444", "width":45},
    {'letter': 'k', 'filling': "#089db2", "width":45},
    {'letter': 'g', 'filling': "#089db2", "width":45},
    {'letter': 'a', 'filling': "#049444", "width":45},
    {'letter': 'ã', 'filling': "#049444", "width":45},
    {'letter': 'ə', 'filling': "#049444", "width":45},
    {'letter': 's', 'filling': "#089db2", "width":45},{'letter': 'z', 'filling': "#089db2", "width":45},
    {'letter': 'f', 'filling': "#089db2", "width":45},{'letter': 'v', 'filling': "#089db2", "width":45},
    {'letter': 'ʃ', 'filling': "#089db2", "width":45},{'letter': 'ʒ', 'filling': "#089db2", "width":45},
    {'letter': 'h', 'filling': "#089db2", "width":45},{'letter': 'ɦ', 'filling': "#089db2", "width":45},
    {'letter': 'x', 'filling': "#089db2", "width":45},{'letter': 'ɣ', 'filling': "#089db2", "width":45},
    {'letter': 'ɺ', 'filling': "#089db2", "width":45},
    {'letter': 'l', 'filling': "#089db2", "width":45},{'letter': 'ʎ', 'filling': "#089db2", "width":45},{'letter': 'ɬ', 'filling': "#089db2", "width":45},
    {'letter': 'n', 'filling': "#089db2", "width":45},{'letter': 'ɲ', 'filling': "#089db2", "width":45},
    {'letter': '\'' , 'filling': "#049444", "width":45},
    {'letter': '.' , 'filling': "#049444", "width":45},
    {'letter': '[' , 'filling': "#049444", "width":45},
    {'letter': ']' , 'filling': "#049444", "width":45},

]
# output do sistema
transcript = []

class MainKeyboard(UserControl):
    def build(self):
        def clear_output(e):
                output_column.clean()
                output_column.update()

        def add_output(e):
                transcript.append({'entrada': input.value})
                if input=='':
                    output_column.controls = [Text(value="Digite uma palavra")]
                else:
                    output_column.controls = [
                        Container(
                            padding=padding.only(left=10),
                            border_radius=border_radius.all(5),
                            height=35,
                            width=300,
                            bgcolor=colors.TEAL_100,
                            content=Text(value=item['entrada'],color="#089db2",size=25, selectable=True),

                        ) for item in transcript]
                    output_column.update()
                    input.value = ''
                    input.update()

        def letter_key(e):
                value_atual = input.value if input.value != '' else ''
                value = e.control.content.value
                input.value = value_atual+ value
                input.update()


        # =========================== Input do usuário ================================= #
        input = TextField(
            value='',label="Input",expand=True, keyboard_type="ipa",
            border_color="#089db2",border_width = 2, border_radius= border_radius.all(20),
            cursor_color=colors.TEAL_500

            )
        # =========================== Output para o usuário ================================= #
        output_column = Column(
                height=200,
                scroll=True,
            )

        # =========================== Teclado virtual ================================= #
        keyboard = Row(
                        wrap = True,
                        spacing=3,
                        alignment = MainAxisAlignment.CENTER,
                        #molde dos botões
                        controls =[
                            Container(
                                content=Text(
                                    value=btn['letter'],
                                    color= colors.BLUE_100,
                                    size=25,
                                    font_family="ipa"),
                                alignment = alignment.center,
                                height=40,
                                width = btn['width'],
                                bgcolor = btn['filling'],
                                border_radius = border_radius.all(10),
                                tooltip= f"botão {btn['letter']}",
                                on_click=letter_key) for btn in btns]
                            )
        # =========================== Layout do programa =================================#
        layout = Column(
                expand=True,
                scroll=True,
                spacing = 20,
                controls = [
                    output_column,
                    Divider(),
                    Row(
                        controls = [
                            input,

                            ElevatedButton(text="Clear", tooltip="Clear",color="#089db2",
                                          on_click=clear_output),
                            IconButton(icons.SEND, tooltip="Enviar",icon_color="white",bgcolor="#089db2",
                                          on_click= add_output),

                        ]
                    ),
                    Divider(),
                    keyboard,
                    ]
                )
        return layout
