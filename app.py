__author__ = 'bender'
import os
import string
import random
import tornado.web
import tornado.ioloop
import tornado.websocket


class MainHandler(tornado.web.RequestHandler):
	def get(self):
		self.render('index.html', messages=None)


class Application(tornado.web.Application):
	def __init__(self):
		handlers = [
			(r'/', MainHandler),
			(r'/static/(.*)', tornado.web.StaticFileHandler,
			{'path': 'static/'})
		]
		settings = dict(
			cookie_secret=''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(35)),
			xsrf_cookies=True,
			debug=True,
			template_path=os.path.join(os.path.dirname(__file__), 'templates'),
			static_path=os.path.join(os.path.dirname(__file__), 'static')
		)
		tornado.web.Application.__init__(self, handlers, **settings)

application = Application()

if __name__ == "__main__":
	application.listen(7766)
	tornado.ioloop.IOLoop.current().start()
