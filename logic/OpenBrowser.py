import webbrowser

def abrir_navegador_con_ip_y_puerto():
    puerto_flask = 5000  # Puerto en el que se ejecuta Flask
    mi_ip_local = "127.0.0.1"  # Dirección IP local
    url = f"http://{mi_ip_local}:{puerto_flask}"
    webbrowser.open(url)
