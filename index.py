#-*- coding:utf-8 -*-

htmlbody='''<!DOCTYPE html>
    <html>
    <head>
    <script type="text/javascript">
    var xmlhttp;
    if (window.XMLHttpRequest) {
        xmlhttp=new XMLHttpRequest();
    } 
    xmlhttp.onreadystatechange= change;
    function change() {
      document.getElementById("content").innerHTML=xmlhttp.responseText;
      try{
         result = window.android.send(xmlhttp.responseText);
      } catch (err){}
    }
    function loadremotefile() {
      var value = document.getElementById("filename").value;
      xmlhttp.open("GET",value,true);
      xmlhttp.send();
    }
    </script>
    </head>
    <body>
    <h2>Vivian's request</h2>
    <hr>
    <div id="content"><P></div>
    <hr>
    <input type="text" value="hello.txt" id="filename"><br>
    <button type="button" onclick="loadremotefile()">Corss XMLHttpRequest</button>
    </body>
    </html>'''

def app(environ, start_response):
    status = '200 OK'
    headers = [('Content-type', 'text/html')]
    start_response(status, headers)
    body=htmlbody
    return body

from bae.core.wsgi import WSGIApplication
application = WSGIApplication(app)
