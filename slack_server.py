import time
from http.server import BaseHTTPRequestHandler, HTTPServer
from io import BytesIO
from urllib.parse import urlparse, parse_qs

from requests_on_REST.add_new_post import add_new_post
from requests_on_REST.add_user_to_chat import add_user_to_chat
from requests_on_REST.add_user_to_forum import add_user_to_forum
from requests_on_REST.chats_for_user_without_forums import \
    chats_for_user_without_forums
from requests_on_REST.chats_inside_forum import chats_inside_forum
from requests_on_REST.create_note import create_note
from requests_on_REST.delete_user import delete_user
from requests_on_REST.get_all_posts_at_forum import get_all_posts_at_chat
from requests_on_REST.get_all_users import get_all_users
from requests_on_REST.get_user_by_id import get_user_by_id_param
from requests_on_REST.read_notes import read_notes
from requests_on_REST.register import register
from requests_on_REST.user_forums import user_forums
from requests_on_REST.delete_note import delete_note
from requests_on_REST.create_chat import create_chat
from requests_on_REST.create_forum import create_forum
from requests_on_REST.update_note import update_note

HOST_PORT = 86


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        full_path = urlparse(self.path)
        path = full_path.path
        qs = parse_qs(full_path.query)

        if path == "/all_users":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(bytes(get_all_users(), "utf-8"))
        else:
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(bytes("Hello World!! - GET RECEIVED", "utf-8"))

    def do_POST(self):
        full_path = urlparse(self.path)
        path = full_path.path
        qs = parse_qs(full_path.query)

        if path == "/user_id":
            '''example path: http://localhost:86/user_id?user_id=1'''
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(bytes(get_user_by_id_param(qs).to_json(
                orient='records', date_format='iso'), "utf-8"))

        elif path == "/chats_inside_forum":
            '''example path: http://localhost:86/chats_inside_forum
            ?upper_forum_id=1 '''
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(bytes(chats_inside_forum(qs).to_json(
                orient='records', date_format='iso'), "utf-8"))

        elif path == "/user_chats":
            '''example path: http://localhost:86/user_chats?user_id=1'''
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(bytes(chats_for_user_without_forums(qs).to_json(
                orient='records', date_format='iso'), "utf-8"))

        elif path == "/user_forums":
            '''example path: http://localhost:86/user_forums?permitted_user
            =1 '''
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(bytes(user_forums(qs).to_json(
                orient='records', date_format='iso'), "utf-8"))

        elif path == "/get_all_posts_at_chats":
            '''example path: http://localhost:86/get_all_posts_at_chats
            ?chat_id=2 '''
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(bytes(get_all_posts_at_chat(qs).to_json(
                orient='records', date_format='iso'), "utf-8"))

        elif path == "/add_new_post":
            '''Body example: {"owner_id": "2", "chat_id": "2", 
            "post_content": "testowy post"} '''
            content_length = int(self.headers['Content-Length'])
            body = self.rfile.read(content_length)
            self.send_response(200)
            self.end_headers()
            add_new_post(body)
            response = BytesIO()
            self.wfile.write(response.getvalue())

        elif path == "/register":
            '''Body example: {"user_name": "test123", "user_surname": 
            "testowy", "login": "test_test", "password": "haslo12345"} '''
            content_length = int(self.headers['Content-Length'])
            body = self.rfile.read(content_length)
            self.send_response(200)
            self.end_headers()
            register(body)
            response = BytesIO()
            self.wfile.write(response.getvalue())

        elif path == "/delete_user":
            '''Body example: {"user_id": "1"}'''
            content_length = int(self.headers['Content-Length'])
            body = self.rfile.read(content_length)
            self.send_response(200)
            self.end_headers()
            delete_user(body)
            response = BytesIO()
            self.wfile.write(response.getvalue())

        elif path == "/add_user_to_chat":
            '''Body example: {"chat_id": "2", "permitted_user": "2"}'''
            content_length = int(self.headers['Content-Length'])
            body = self.rfile.read(content_length)
            self.send_response(200)
            self.end_headers()
            add_user_to_chat(body)
            response = BytesIO()
            self.wfile.write(response.getvalue())

        elif path == "/add_user_to_forum":
            '''Body example: {"forum_id": "2", "permitted_user": "2"}'''
            content_length = int(self.headers['Content-Length'])
            body = self.rfile.read(content_length)
            self.send_response(200)
            self.end_headers()
            add_user_to_forum(body)
            response = BytesIO()
            self.wfile.write(response.getvalue())

        elif path == "/create_note":
            '''Body example: {"title": "druga próba", "notes_content": 
            "Ziomki są na pierwszym miejscu.", "owner_id": 2} '''
            content_length = int(self.headers['Content-Length'])
            body = self.rfile.read(content_length)
            self.send_response(200)
            self.end_headers()
            create_note(body)
            response = BytesIO()
            self.wfile.write(response.getvalue())

        elif path == "/read_notes":
            '''example path: http://localhost:86/read_notes?owner_id=1'''
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(bytes(read_notes(qs).to_json(
                orient='records', date_format='iso'), "utf-8"))

        elif path == "/delete_note":
            '''Body example: {"note_id": "10"}'''
            content_length = int(self.headers['Content-Length'])
            body = self.rfile.read(content_length)
            self.send_response(200)
            self.end_headers()
            delete_note(body)
            response = BytesIO()
            self.wfile.write(response.getvalue())

        elif path == "/update_note":
            content_length = int(self.headers['Content-Length'])
            body = self.rfile.read(content_length)
            self.send_response(200)
            self.end_headers()
            update_note(body)
            response = BytesIO()
            self.wfile.write(response.getvalue())

        elif path == "/create_chat":
            '''Body example: {"upper_forum_id": "1", "chat_name":  
            "example chat", "image": "1"} '''
            content_length = int(self.headers['Content-Length'])
            body = self.rfile.read(content_length)
            self.send_response(200)
            self.end_headers()
            create_chat(body)
            response = BytesIO()
            self.wfile.write(response.getvalue())

        elif path == "/create_forum":
            '''Body example: {"forum_name": "kolejne", "image": "2"} '''
            content_length = int(self.headers['Content-Length'])
            body = self.rfile.read(content_length)
            self.send_response(200)
            self.end_headers()
            create_forum(body)
            response = BytesIO()
            self.wfile.write(response.getvalue())

        else:
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(bytes("POST RECEIVED", "utf-8"))


def connection():
    my_server = HTTPServer(('', HOST_PORT), MyServer)
    print(time.asctime(), "Server Slack Starts - %s:%s" % ('', HOST_PORT))

    try:
        my_server.serve_forever()

    except KeyboardInterrupt:
        pass

    my_server.server_close()
    print(time.asctime(), "Server Stops - %s:%s" % ('', HOST_PORT))


if __name__ == '__main__':
    connection()
