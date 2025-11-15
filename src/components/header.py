import flet as ft


class Header(ft.Container):
    """
    A header component that displays a title and optional subtitle.

    By default this header expands to fill available width (expand=True).
    You can override expand or pass other ft.Container kwargs.
    """
    def __init__(
        self,
        title: str,
        subtitle: str | None = None,
        expand: bool = True,
        **kwargs
    ):
        header_content = ft.Row(
            [
                ft.Text(title, style="headlineMedium"),
                ft.Text(
                    subtitle, style="bodyMedium"
                )
                if subtitle
                else ft.Container(),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )

        super().__init__(
            header_content,
            expand=expand,
            padding=ft.padding.all(16),
            bgcolor=ft.Colors.BLUE_200,
            **kwargs,
        )
