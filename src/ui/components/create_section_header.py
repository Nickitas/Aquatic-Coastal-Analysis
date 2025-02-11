from nicegui import ui

def create_section_header(title: str, subtitle: str, heading_level: int = 1, sep: bool = True) -> None:
    """
    Создаёт раздел с заголовком и подзаголовком.
      - 'title': большой жирный заголовок (размер зависит от heading_level)
      - 'subtitle': более мелкий текст под ним
    heading_level: 1, 2 или 3 (по умолчанию 1).
    """
    # Карта уровней заголовка к Tailwind-классам
    heading_classes_map = {
        1: 'text-3xl font-bold mt-3 mb-1 text-zinc-900 dark:text-zinc-100',
        2: 'text-2xl font-bold mt-2 text-zinc-900 dark:text-zinc-100',
        3: 'text-xl font-bold mt-1 text-zinc-900 dark:text-zinc-100'
    }

    heading_classes = heading_classes_map.get(heading_level, heading_classes_map[1])

    ui.label(title).classes(heading_classes)
    ui.label(subtitle).classes('text-md text-zinc-800 dark:text-zinc-200')
    if (sep): ui.separator().classes('bg-slate-200 dark:bg-slate-700')
