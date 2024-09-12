from pelican import signals

def clean_title(instance):
    if hasattr(instance, 'title'):
        title = instance.title
        if isinstance(title, str):
            if title.startswith("'") and title.endswith("'"):
                instance.title = title[1:-1]
            elif title.startswith('"') and title.endswith('"'):
                instance.title = title[1:-1]

def register():
    signals.content_object_init.connect(clean_title)
