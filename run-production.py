# noinspection PyUnresolvedReferences


if __name__ == '__main__':
    from onlineoffice import app
    # noinspection PyPackageRequirements
    from gevent.pywsgi import WSGIServer

    WSGIServer(('0.0.0.0', 8080), app).serve_forever()
