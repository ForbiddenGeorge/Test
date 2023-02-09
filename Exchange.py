import flet as ft
import requests


def Exchange(page, ft=ft):
    def klikl(e):

        ZToho = str(PrvniMena.value)
        ZToho = ZToho[0:3]
        DoToho = str(DruhaMena.value)
        DoToho = DoToho[0:3]
        response = requests.get(
            f"https://api.frankfurter.app/latest?amount={prvni.value}&from={ZToho}&to={DoToho}")

        druha.value = response.json()['rates'][DoToho]
        page.update()

    prvni = ft.TextField(label="Hodnota",on_submit=klikl)

    druha = ft.TextField(label="Hodnota", icon=ft.icons.ARROW_RIGHT, on_submit=None)
    PrvniMena = ft.Dropdown(
        width=300,
        label="Měna",
        options=[
            ft.dropdown.Option("USD (Americký dolar)"),
            ft.dropdown.Option("EUR (euro)"),
            ft.dropdown.Option("GBP (Britská libra)"),
            ft.dropdown.Option("JPY (Japonksý jen)"),
            ft.dropdown.Option("CZK (Česká koruna)"),
            ft.dropdown.Option("CHF (Švýcarský frank)"),
            ft.dropdown.Option("CNY (Čínský renminbi)"),
            ft.dropdown.Option("MXN (Mexické peso)"),
            ft.dropdown.Option("INR (Indická rupie)"),
            ft.dropdown.Option("PHP (Filipínské peso)"),
            ft.dropdown.Option("TRY (Turecká lira)"),
            ft.dropdown.Option("CAD (Kanadský dolar)"),
            ft.dropdown.Option("AUD (Austraslý dolar)"),
            ft.dropdown.Option("HUF (Maďarský florint)"),
            ft.dropdown.Option("DKK (Dánská koruna)")
        ]
    )
    DruhaMena = ft.Dropdown(
        width=300,
        label="Měna",
        icon = ft.icons.CURRENCY_EXCHANGE,
        options=[
            ft.dropdown.Option("USD (Americký dolar)"),
            ft.dropdown.Option("EUR (euro)"),
            ft.dropdown.Option("GBP (Britská libra)"),
            ft.dropdown.Option("JPY (Japonksý jen)"),
            ft.dropdown.Option("CZK (Česká koruna)"),
            ft.dropdown.Option("CHF (Švýcarský frank)"),
            ft.dropdown.Option("CNY (Čínský renminbi)"),
            ft.dropdown.Option("MXN (Mexické peso)"),
            ft.dropdown.Option("INR (Indická rupie)"),
            ft.dropdown.Option("PHP (Filipínské peso)"),
            ft.dropdown.Option("TRY (Turecká lira)"),
            ft.dropdown.Option("CAD (Kanadský dolar)"),
            ft.dropdown.Option("AUD (Austraslý dolar)"),
            ft.dropdown.Option("HUF (Maďarský florint)"),
            ft.dropdown.Option("DKK (Dánská koruna)")
        ]
    )
    ups = ft.Text("koko")
    contenty = ft.Column(
        [
               ft.Row(
                 [
                    ft.Column(

                        [
                            PrvniMena,
                            prvni
                        ]
                    ),
                    ft.Column(
                        [
                            DruhaMena,
                            druha
                        ]
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Row(
                [
                    ft.ElevatedButton(content=(ft.Text("Převeď",size=20)), on_click=klikl)
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
        ]
    )

    return contenty