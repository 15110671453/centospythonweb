import web
urls = ('/','index')

class index:
	def GET(self):
		return "HELLO,world!python"
if __name__ == "__main__": 
		app = web.application(urls,globals())
		app.run()