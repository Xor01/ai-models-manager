class LoggingMixin():
    """Mixin class to provide logging functionality."""
    def log(self, message):
        print(f"[LOG] {message}")
