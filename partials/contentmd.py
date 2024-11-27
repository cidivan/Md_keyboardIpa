from flet import UserControl,TextField, Row, Container, padding, border_radius, colors,Markdown, MarkdownExtensionSet

#class EditorMd(UserControl):
 #   def build(self):
def update_view(e):
            view_md.content.value = e.control.value
            view_md.update()

editor_md = TextField(
            expand=True,
            multiline=True,
            min_lines=20,
            max_lines=20,
            content_padding=padding.all(30),
            border_radius=border_radius.all(10),
            border_color=colors.TEAL_500,
            bgcolor=colors.TEAL_100,
            on_change=update_view
        )
view_md = Container(
            border_radius=border_radius.all(10),
            padding=padding.all(30),
            expand=True,
            bgcolor=colors.TEAL_100,
            content=Markdown(
                value=editor_md.value,
                selectable=True,
                extension_set=MarkdownExtensionSet.GITHUB_WEB,
                code_theme='monokai-sublime'
        ))
linha_md = Row(
            controls=[
                editor_md,
                view_md
            ]
        )
        #return linha_md