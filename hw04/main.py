import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self,m,n):

        if m is not None:
            m = int(m)
            if m <= 9: 
                n = int(n) if n is not None else m
        else:
            m = 9 
            n = 9

        html='''
        <html>
        <body>
        <table>
        '''
        
        for i in range(1,m+1):
            html += '<TR>'
            for j in range(1,n+1):
                html += '<td>%d*</td>' %i
                html += '<td>%d=</td>' %j
                html += '<td>%d</td>' %(i*j)
                
            html += '</TR>'

        html += '''
        </table>
        </body>
        </html>
        '''
        self.write(html)

application = tornado.web.Application([
    (r"/(?:([0-9]+)(?:/([0-9]+))?)?", MainHandler),
], debug=True) 

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

    
