import os
import re

directory = r'C:\Users\starl\Desktop\personal\Unphu\cuatrimestre 5\Programacion web\Proyecto final\Programacion-web-UNPHU\Proyecto_django\configuration\mi_web\templates'

mappings = {
    r'index\.html': "{% url 'index' %}",
    r'noticias\.html': "{% url 'noticias' %}",
    r'enlaces\.html': "{% url 'enlaces' %}",
    r'contacto\.html': "{% url 'contacto' %}",
    r'[Bb]ulbasaur\.html': "{% url 'bulbasaur' %}",
    r'[Cc]harmander\.html': "{% url 'charmander' %}",
    r'[Ss]quirtle\.html': "{% url 'squirtle' %}"
}

def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Add {% load static %} if not present
    if '{% load static %}' not in content:
        content = '{% load static %}\n' + content

    # Replace CSS links
    content = content.replace('../Multimedia/CSS/', "{% static 'css/' %}")
    
    # Replace JS script
    content = content.replace('../Funcionalidad/App.js', "{% static 'js/App.js' %}")

    # Replace images
    content = content.replace('../Multimedia/IMG/', "{% static 'img/' %}")
    # Also handle img/ if it appears in noticias.html (as seen before)
    # But only if it looks like a relative path to static
    # content = content.replace('src="img/', 'src="{% static \'img/\'}') 
    # Let's stick to the prompt's specific instructions first.
    # The prompt says: "check for ../Multimedia/IMG/ and replace with {% static 'img/' %}"

    # Replace relative links in href
    for pattern, replacement in mappings.items():
        # Match href="pattern" or href='pattern'
        # Using regex to ensure we only replace within href
        content = re.sub(f'href=["\']{pattern}["\']', f'href="{replacement}"', content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

for filename in os.listdir(directory):
    if filename.endswith('.html'):
        update_file(os.path.join(directory, filename))
