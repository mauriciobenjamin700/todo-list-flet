import flet as ft


class CenterContainer(ft.Container):
    """
    A container that centers its content both vertically and horizontally.

    By default this container expands to fill available space (expand=True).
    You can override expand or pass other ft.Container kwargs.
    """
    def __init__(self, content: ft.Control, *, expand: bool = True, **kwargs):
        # forward common container kwargs and set sensible defaults
        super().__init__(
            content,
            expand=expand,
            alignment=ft.alignment.center,
            **kwargs,
        )


class VerticalContainer(ft.Container):
    """
    A container that arranges its children vertically and centers them.
    """
    def __init__(self, controls: list[ft.Control]):
        super().__init__(
            ft.Column(
                controls,
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )


class HorizontalContainer(ft.Container):
    """
    A container that arranges its children horizontally and centers them.
    """
    def __init__(self, controls: list[ft.Control]):
        super().__init__(
            ft.Row(
                controls,
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )
