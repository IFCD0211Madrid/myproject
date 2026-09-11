class MobilePhone:
    # Anotaciones de tipo a nivel de clase (opcionales)
    manufacturer: str
    screen_size: float
    num_cores: int
    apps: list
    status: bool

    def __init__(self, manufacturer: str, screen_size: float, num_cores: int):
        self.manufacturer = manufacturer
        self.screen_size = screen_size
        self.num_cores = num_cores
        self.apps = []         # Lista independiente para cada objeto
        self.status = False    # Apagado por defecto

    def power_on(self):
        self.status = True

    def power_off(self):
        self.status = False

    def install_app(self, *apps: str):
        """Instala una o varias aplicaciones (acepta cadenas individuales o múltiples argumentos)."""
        for app in apps:
            if app not in self.apps:
                self.apps.append(app)

    def uninstall_app(self, *apps: str):
        """Desinstala una o varias aplicaciones."""
        for app in apps:
            if app in self.apps:
                self.apps.remove(app)
    

