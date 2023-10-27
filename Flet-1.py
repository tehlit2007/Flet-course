# Курс по Flet
import flet as ft


def main(page: ft.Page):
    page.title = "Моя программа"
    t = ft.Text("Привет, интерфейс Flet!")
    page.controls.append(t)
    page.update()


ft.app(main)
