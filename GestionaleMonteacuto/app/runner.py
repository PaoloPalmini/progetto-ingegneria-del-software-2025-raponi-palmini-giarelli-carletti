def run():
    """Run the application by delegating to the package main."""
    try:
        from ..GestionaleMonteacuto import main
    except Exception:
        # fallback if executed as script
        from GestionaleMonteacuto import main
    main()
