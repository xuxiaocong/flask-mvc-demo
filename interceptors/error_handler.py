from application import app


@app.errorhandler(404)
def error_404(e):
    return dict(message="404 not found")