class BaseView:
    """Simple base view. Implement UI rendering in concrete views."""

    def render(self, data):
        raise NotImplementedError("render must be implemented by subclasses")
