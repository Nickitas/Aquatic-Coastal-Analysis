from nicegui import ui

def create_section_header(title: str, subtitle: str, heading_level: int = 1) -> None:
    """
    Создаёт раздел с заголовком и подзаголовком.
      - 'title': большой жирный заголовок (размер зависит от heading_level)
      - 'subtitle': более мелкий текст под ним
    heading_level: 1, 2 или 3 (по умолчанию 1).
    """
    # Карта уровней заголовка к Tailwind-классам
    heading_classes_map = {
        1: 'text-3xl font-bold mt-4 mb-1',
        2: 'text-2xl font-bold mt-3 mb-1',
        3: 'text-xl font-bold mt-2 mb-1'
    }

    heading_classes = heading_classes_map.get(heading_level, heading_classes_map[1])

    ui.label(title).classes(heading_classes)
    ui.label(subtitle).classes('text-md text-gray-600 mb-4')
