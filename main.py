import flet as ft

def main (page: ft.Page):
    page.title = "Meu Primeiro app Flet"
    page.bgcolor = "#e010c8"
    page.vertical_alignment = ft.CrossAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.add(
        ft.Text(value="Yan Remedi"),
        ft.ElevatedButton("Clique Aqui")
    )

ft.run(main)